import streamlit as st

def consultar_modelo(cliente, mensajes, modelo, temperatura):
    try:
        respuesta = cliente.chat.completions.create(
            model=modelo,
            messages=mensajes,
            temperature=temperatura,
            max_tokens=1024,
        )
        return respuesta.choices[0].message.content
    except Exception as error:
        return f"Error: {str(error)}"