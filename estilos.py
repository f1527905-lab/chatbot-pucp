import streamlit as st

def aplicar_estilos():
    st.markdown("""
    <style>
    /* ==================== ESTILOS GENERALES ==================== */
    .stApp {
        background-color: #f5f7fa;
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* ==================== HEADER IZQUIERDO ==================== */
    .header-pucp-izquierdo {
        background: linear-gradient(135deg, #003d82 0%, #0056b3 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 4px 15px rgba(0, 61, 130, 0.2);
        text-align: center;
        margin-bottom: 20px;
    }
    
    .universidad {
        font-size: 36px;
        font-weight: 900;
        letter-spacing: 4px;
        margin-bottom: 8px;
    }
    
    .educacion-continua {
        font-size: 16px;
        font-weight: 600;
        letter-spacing: 2px;
        opacity: 0.95;
    }
    
    /* ==================== HEADER DEL CHAT ==================== */
    .chat-header-azul {
        background: linear-gradient(135deg, #003d82 0%, #0056b3 100%);
        padding: 20px 25px;
        color: white;
        border-radius: 15px 15px 0 0;
        box-shadow: 0 4px 15px rgba(0, 61, 130, 0.2);
        margin-bottom: 0;
    }
    
    .chat-title-azul {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }
    
    .chat-title-azul h2 {
        margin: 0;
        font-size: 22px;
        font-weight: 700;
    }
    
    .status-online {
        background: rgba(76, 175, 80, 0.3);
        color: #4caf50;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
    }
    
    .chat-subtitle-azul {
        margin: 0;
        opacity: 0.9;
        font-size: 13px;
    }
    
    /* ==================== ESTILOS DEL CONTAINER NATIVO ==================== */
    /* El container de Streamlit con height=700 */
    [data-testid="stVerticalBlock"] > div:has(.mensajes-area) {
        background: white !important;
        border-radius: 0 0 15px 15px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        scroll-behavior: smooth !important;
        padding: 20px !important;
    }
    
    /* Scrollbar personalizado para el container */
    [data-testid="stVerticalBlock"] > div:has(.mensajes-area)::-webkit-scrollbar {
        width: 6px;
    }
    
    [data-testid="stVerticalBlock"] > div:has(.mensajes-area)::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    [data-testid="stVerticalBlock"] > div:has(.mensajes-area)::-webkit-scrollbar-thumb {
        background: #003d82;
        border-radius: 10px;
    }
    
    [data-testid="stVerticalBlock"] > div:has(.mensajes-area)::-webkit-scrollbar-thumb:hover {
        background: #0056b3;
    }
    
    /* Área de mensajes */
    .mensajes-area {
        padding: 10px;
    }
    
    /* Animación de fade in */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* ==================== INPUT DE CHAT ==================== */
    .stChatInputContainer {
        background: white !important;
        border: 2px solid #003d82 !important;
        border-radius: 25px !important;
        box-shadow: 0 2px 10px rgba(0, 61, 130, 0.1) !important;
        margin-top: 0 !important;
    }
    
    .stChatInput textarea {
        border: none !important;
    }
    
    /* ==================== BOTONES ==================== */
    .stButton > button {
        width: 100%;
        background: white;
        color: #003d82;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 10px 15px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: #003d82;
        color: white;
        border-color: #003d82;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 61, 130, 0.3);
    }
    
    /* ==================== OCULTAR ELEMENTOS ==================== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* ==================== RESPONSIVE ==================== */
    @media (max-width: 768px) {
        .universidad {
            font-size: 28px;
        }
    }
    
    </style>
    """, unsafe_allow_html=True)

