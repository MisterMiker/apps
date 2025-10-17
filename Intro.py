import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json

# ---- CONFIGURACIÓN DE LA PÁGINA ----
st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide"
)

# ---- ESTILO VISUAL (Tema claro/oscuro) ----
theme = st.radio("Elige un tema:", ["Claro", "Oscuro"], horizontal=True)

if theme == "Oscuro":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0d1117;
            color: white;
        }
        a { color: #58a6ff !important; }
        h1, h2, h3, h4, h5 {
            color: #c9d1d9;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #e9f5f9;
            color: #0d3b66;
            font-family: "Segoe UI", sans-serif;
        }
        h1, h2, h3 {
            color: #144552;
        }
        a {
            color: #0d3b66 !important;
            font-weight: bold;
            text-decoration: none;
        }
        a:hover {
            color: #3a86ff !important;
            text-decoration: underline;
        }
        </style>
    """, unsafe_allow_html=True)

# ---- TÍTULO PRINCIPAL ----
st.title("🤖 Aplicaciones de Inteligencia Artificial")

# ---- SIDEBAR ----
with st.sidebar:
    st.subheader("💡 Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# ---- ENLACE PRINCIPAL ----
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("🌐 En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"🔗 Enlace para páginas y ejercicios: [Haz clic aquí]({url_ia})")

# ---- PESTAÑAS DE ORGANIZACIÓN ----
tabs = st.tabs(["🎙️ Voz y Lenguaje", "🧠 Análisis e Imagen", "🤝 Control y Hardware"])

# ---- COLUMNA 1 ----
with tabs[0]:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🗣️ Conversión de texto a voz")
        image = Image.open('1.png')
        st.image(image, width=190)
        st.write("Aplicación para presentar auditivamente un texto") 
        url = "https://mwcvogxsfresrryrvr8akq.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("😃 Reconimiento de emociones")
        image = Image.open('sticker.png')
        st.image(image, width=200)
        st.write("La presente página busca encontrar la emoción en frases y palabras") 
        url = "https://pae4apprbctyuk29tykpwim.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("🧾 Reconocimiento de texto en cámara")
        image = Image.open('images (1).jpeg')
        st.image(image, width=200)
        st.write("Pon un texto en tu webcam y este aplicativo lo leerá") 
        url = "https://eb4up7c6bdvnixezsf3uny.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("🔢 Reconocimiento de dígitos")
        image = Image.open('9.png')
        st.image(image, width=200)
        st.write("Escribe un número y el aplicativo lo leerá") 
        url = "https://guw5hbkuplisckimsesffz.streamlit.app/"
        st.write(f"[Enlace]({url})")

    with col2:
        st.subheader("🎧 Traductor de voz")
        image = Image.open('309206.png')
        st.image(image, width=200)
        st.write("La siguiente aplicación traducirá en texto una entrada del micrófono") 
        url = "https://9wxumiwaxls2hderp86v7r.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("🧩 Análisis de texto")
        image = Image.open('a.jpeg')
        st.image(image, width=200)
        st.write("El siguiente aplicativo busca poder responder preguntas sobre un texto subido por el usuario") 
        url = "https://unyf7bynmkmepwxavgyodj.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("📚 Análisis de texto en ESPAÑOL")
        image = Image.open('España.png')
        st.image(image, width=200)
        st.write("El siguiente aplicativo busca poder responder preguntas sobre un texto subido por el usuario") 
        url = "https://tdfesp-jjkfuksktwe2chktberohb.streamlit.app/"
        st.write(f"[Enlace]({url})")

# ---- COLUMNA 2 ----
with tabs[1]:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Reconocimiento de objetos en cámara")
        image = Image.open('B.jpeg')
        st.image(image, width=200)
        st.write("Presencia el poder de la inteligencia artificial para reconocer objetos en una imagen") 
        url = "https://yolov5-xmswsvv5xzm3m8kfmdyj7i.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("🖼️ Análisis de Imagen")
        image = Image.open('A.png')
        st.image(image, width=200)
        st.write("Presencia la capacidad de la computadora para analizar imágenes") 
        url = "https://visionapp-urkrnqmwncrsutrupqwajo.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("📖 Lector de texto en imágenes")
        image = Image.open('AA.jpg')
        st.image(image, width=200)
        st.write("Sube una imagen y el aplicativo la leerá") 
        url = "https://ocr-audio-mqj9rbmpiblmmbdyb8xpc2.streamlit.app/"
        st.write(f"[Enlace]({url})")

    with col2:
        st.subheader("📘 Guía de cultivo de Glorps con PDF")
        image = Image.open('images.jpeg')
        st.image(image, width=190)
        st.write("Con base a un PDF veremos cómo cultivar glorps :D") 
        url = "https://chatpdf-cgep6dpyw9zi5gzx5kvnmx.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("🎨 Tablero inteligente")
        image = Image.open('Tablerito.png')
        st.image(image, width=200)
        st.write("Este aplicativo reconoce lo que el usuario dibuje en un pequeño tablero") 
        url = "https://histinf-6tgf3nnhwuwas2wqmufaqi.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("🧠 Tablero simple")
        image = Image.open('Ay.png')
        st.image(image, width=200)
        st.write("Este es un aplicativo de un tablero básico") 
        url = "https://tablerito-xd5bgynb7kv6grohtbkq5r.streamlit.app/"
        st.write(f"[Enlace]({url})")

# ---- COLUMNA 3 ----
with tabs[2]:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🖐️ Reconocimiento de gestos con manos")
        image = Image.open('Paloma.png')
        st.image(image, width=190)
        st.write("Esta aplicación busca reconocer uno de tres gestos con las manos") 
        url = "https://detectorgestosmiguel.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("💻 Computadora funcional con voz")
        image = Image.open('Micro.png')
        st.image(image, width=200)
        st.write("Este aplicativo permite el uso de una microcomputadora o aplicación de Wowki con voz") 
        url = "https://ctrlvoice-5jd4q2bypdhylkwzqhqv7r.streamlit.app/"
        st.write(f"[Enlace]({url})")

    with col2:
        st.subheader("🔌 Controlador de microcomputadora")
        image = Image.open('Elgato.png')
        st.image(image, width=200)
        st.write("Este aplicativo controlará una microcomputadora física o de wowki") 
        url = "https://sendcmqtt-vuzekwrhsv4svewg4hsr44.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("📡 Receptor de MQTT")
        image = Image.open('Receptor.png')
        st.image(image, width=200)
        st.write("Lee información enviada desde una microcomputadora o una aplicación de wowki") 
        url = "https://recepmqtt-8fvjh4tsjnxaxafjy3qok3.streamlit.app/"
        st.write(f"[Enlace]({url})")

        st.subheader("🧪 Prueba 1")
        image = Image.open('Silly.jpg')
        st.image(image, width=200)
        st.write("Esta fue una aplicación inicial para conocer el panorama de Github y Streamlit") 
        url = "https://miprimerappsoyunvictorioso.streamlit.app/"
        st.write(f"[Enlace]({url})")

# ---- PIE DE PÁGINA ----
st.markdown("""
---
📘 *Aplicación creada por [Tu Nombre]*  
🚀 Desarrollada con [Streamlit](https://streamlit.io/)
""", unsafe_allow_html=True)
