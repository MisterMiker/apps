import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de texto a voz")
 image = Image.open('1.png')
 st.image(image, width=190)
 st.write("Aplicación para presentar auditivamente un texto") 
 url = "https://mwcvogxsfresrryrvr8akq.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Reconimiento de emociones")
 image = Image.open('sticker.png')
 st.image(image, width=200)
 st.write("La presente página busca encontrar la emoción en frases y palabras") 
 url = "https://pae4apprbctyuk29tykpwim.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Reconocimiento de objetos en cámara")
 image = Image.open('B.jpeg')
 st.image(image, width=200)
 st.write("En esta aplicación presenciarás el poder de la inteligencia artificial para reconocer objetos en una imagen") 
 url = "https://yolov5-xmswsvv5xzm3m8kfmdyj7i.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Reconocimiento de texto en cámara")
 image = Image.open('images (1).jpeg')
 st.image(image, width=200)
 st.write("Pon un texto en tu webcam y este aplicativo lo leerá") 
 url = "https://eb4up7c6bdvnixezsf3uny.streamlit.app/"
 st.write(f"[Enlace]({url})")

with col2: 
 st.subheader("Traductor de voz")
 image = Image.open('309206.png')
 st.image(image, width=200)
 st.write("La siguiente aplicación traducirá en texto una entrada del microfono") 
 url = "https://9wxumiwaxls2hderp86v7r.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Reconocimiento de gestos con manos")
 image = Image.open('Paloma.png')
 st.image(image, width=190)
 st.write("Esta aplicación busca reconocer uno de tres gestos con las manos") 
 url = "https://detectorgestosmiguel.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Análisis de texto")
 image = Image.open('a.jpeg')
 st.image(image, width=200)
 st.write("El siguiente aplicativo busca poder responder preguntas sobre un texto subido por el usuario") 
 url = "https://unyf7bynmkmepwxavgyodj.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Tablero")
 image = Image.open('a.jpeg')
 st.image(image, width=200)
 st.write("Este es un aplicativo de un tablero") 
 url = "https://tablerito-xd5bgynb7kv6grohtbkq5r.streamlit.app/"
 st.write(f"[Enlace]({url})")

with col3: 
 st.subheader("Guía de cultivo de Glorps con PDF")
 image = Image.open('images.jpeg')
 st.image(image, width=190)
 st.write("Ahora, con base a un PDF veremos cómo cultivar glorps :D") 
 url = "https://chatpdf-cgep6dpyw9zi5gzx5kvnmx.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('A.png')
 st.image(image, width=200)
 st.write("En la presente aplicación se podrá presenciar la capacidad de la computadora para analizar imágenes") 
 url = "https://visionapp-urkrnqmwncrsutrupqwajo.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Prueba 1")
 image = Image.open('Silly.jpg')
 st.image(image, width=200)
 st.write("Esta fue una aplicación inicial para conocer el panorama de Github y Streamlit") 
 url = "https://miprimerappsoyunvictorioso.streamlit.app/"
 st.write(f"[Enlace]({url})")


