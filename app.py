import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("facilmente puedo realizar backend y frontend:")
image = Image.open("gato.jpg")

st.image(image, caption="GATO")


texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("Texto ingresado:", texto)

st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto")
with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual","Auditiva", "Tactil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audicion es fundamental para tu interfaz")
  if modo == "Tactil":
    st.write("El tacto es fundamental para tu interfaz")

st.subheader("Uso de Botones")
if st.button("Presiona el botón"):
      st.write("Gracias por presionar")
else:
  st.write("No has presionado eso")

st.subheader("Selectbox")
in_mod = st.selectbox("Selecciona la modalidad", ("Audio", "Visual", "Háptico"),)



if in_mod == "Audio":
  set_mod = "Reproducir audio"
elif in_mod == "Visual":
  set_mod = "Reproducir Video"
elif in_mod == "Háptico":
  set_mod = "Activar la vibración"
st.write("La acción es:",set_mod)
