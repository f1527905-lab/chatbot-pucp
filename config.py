import os
from dotenv import load_dotenv
import streamlit as st

def cargar_api_key():
    """Carga la API key de forma segura"""
    try:
        load_dotenv()
        clave = os.getenv("GROQ_API_KEY")
        if not clave:
            clave = st.secrets.get("GROQ_API_KEY")
        return clave
    except:
        return st.secrets.get("GROQ_API_KEY")

CURSOS = {
    1: {
        "titulo": "Linux y Python desde Cero",
        "precio_gen": 720,
        "precio_pucp": 650,
        "duracion": "8 semanas",
        "horario": "Lunes y miércoles 7:00 pm - 9:00 pm",
        "inicio": "15 de enero 2025"
    },
    2: {
        "titulo": "Excel con Macros y VBA",
        "precio_gen": 450,
        "precio_pucp": 370,
        "duracion": "6 semanas", 
        "horario": "Martes y jueves 6:30 pm - 8:30 pm",
        "inicio": "20 de enero 2025"
    },
    3: {
        "titulo": "Diseño de Cursos Virtuales",
        "precio_gen": 450,
        "precio_pucp": 370,
        "duracion": "6 semanas",
        "horario": "Sábados 9:00 am - 1:00 pm", 
        "inicio": "18 de enero 2025"
    }
}