import os
import streamlit as st
from groq import Groq

from config import cargar_api_key
from estilos import aplicar_estilos
from prompts import SISTEMA_PROMPT, MENSAJE_BIENVENIDA
from chatbot import consultar_modelo


st.set_page_config(
    page_title="Educación Continua PUCP - Chatbot",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    aplicar_estilos()
    

    api_key = cargar_api_key()
    if not api_key:
        st.error("No se pudo cargar la configuración de la API.")
        return
    
    try: 
        cliente_groq = Groq(api_key=api_key)
    except Exception as e:
        st.error(f" Error al inicializar el cliente Groq: {e}")
        return
    

    col_izquierda, col_derecha = st.columns([1, 2])
    
    with col_izquierda:
        mostrar_header_izquierdo()
    
    with col_derecha:
        modelo, temperatura = configurar_sidebar()
        mostrar_chat_mejorado(cliente_groq, modelo, temperatura)


def mostrar_header_izquierdo():
    """Encabezado PUCP sin menú de opciones"""
    st.markdown("""
    <div class="header-pucp-izquierdo">
        <div class="universidad">PUCP</div>
        <div class="educacion-continua">EDUCACIÓN CONTINUA</div>
    </div>
    """, unsafe_allow_html=True)

def configurar_sidebar():
    """Configuración del modelo en sidebar"""
    with st.sidebar:
        st.markdown("###  Configuración del Chatbot")
        
        modelo = st.selectbox(
            "Modelo:",
            ["llama-3.1-8b-instant", "llama-3.1-70b-versatile"],
            index=0
        )
        
        temperatura = st.slider(
            "Creatividad:",
            0.0, 1.0, 0.3, 0.1
        )
        
        if st.button(" Limpiar chat", use_container_width=True):
            st.session_state.historial_chat = []
            st.rerun()
    
    return modelo, temperatura

def mostrar_chat_mejorado(cliente, modelo, temperatura):
    """Chat usando container nativo de Streamlit con altura fija"""
    
    # Inicializar historial
    if "historial_chat" not in st.session_state:
        st.session_state.historial_chat = [{
            "role": "assistant",
            "content": MENSAJE_BIENVENIDA
        }]
    

    st.markdown("""
    <div class="chat-header-azul">
        <div class="chat-title-azul">
            <h2>Asistente Virtual PUCP</h2>
            <span class="status-online">● En línea</span>
        </div>
        <p class="chat-subtitle-azul">
            Estoy aquí para ayudarte con información sobre nuestros cursos.
        </p>
    </div>
    """, unsafe_allow_html=True)

    chat_container = st.container(height=700, border=False)
    
    with chat_container:

        st.markdown('<div class="mensajes-area" id="mensajes-container">', unsafe_allow_html=True)
        
 
        for mensaje in st.session_state.historial_chat:
            if mensaje["role"] == "user":
                st.markdown(f"""
                <div style="display: flex; justify-content: flex-end; margin-bottom: 15px; animation: fadeIn 0.3s ease-out;">
                    <div style="max-width: 70%; background: linear-gradient(135deg, #003d82 0%, #0056b3 100%); color: white; padding: 12px 18px; border-radius: 18px 18px 5px 18px; font-size: 14px; line-height: 1.5; box-shadow: 0 2px 8px rgba(0, 61, 130, 0.2); word-wrap: break-word;">
                        {mensaje["content"]}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                contenido = mensaje["content"].replace("\n", "<br>")
                st.markdown(f"""
                <div style="display: flex; justify-content: flex-start; margin-bottom: 15px; animation: fadeIn 0.3s ease-out;">
                    <div style="max-width: 70%;">
                        <div style="background: #f8f9fa; color: #2c3e50; padding: 12px 18px; border-radius: 18px 18px 18px 5px; font-size: 14px; line-height: 1.5; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); border-left: 4px solid #003d82; word-wrap: break-word;">
                            {contenido}
                        </div>
                        <div style="font-size: 10px; color: #7f8c8d; margin-top: 6px; padding-left: 5px; font-weight: 600;">Asistente PUCP</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
   
    st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)
    

    pregunta = st.chat_input("Escribe tu mensaje aquí...")
    

    if pregunta and pregunta.strip() != "":
        st.session_state.historial_chat.append({
            "role": "user",
            "content": pregunta
        })
        
        mensajes_modelo = [{"role": "system", "content": SISTEMA_PROMPT}] + st.session_state.historial_chat
        
        with st.spinner(" El asistente está escribiendo..."):
            respuesta = consultar_modelo(cliente, mensajes_modelo, modelo, temperatura)
        
        st.session_state.historial_chat.append({
            "role": "assistant",
            "content": respuesta
        })
        
        st.rerun()

if __name__ == "__main__":
    main()