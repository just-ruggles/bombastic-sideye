import streamlit as st
from PIL import Image

st.markdown("<h1 style='color: red;'>Mi primera app (Peter Parker estaría orgulloso)</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='color: blue;'>En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales. O para salvar al mundo, FNSM app en camino.</h2>", unsafe_allow_html=True)
st.write("facilmente puedo realizar backend y frontend:")
image = Image.open("spider-cat.jpg")

st.image(image, caption="MILES-MEWRALES")


texto = st.text_input("Escribe algo", "Miles Morales es el mejor Spider-man")
st.write("Texto ingresado:", texto)

st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Spider-man es un amigo y vecino de la gente :)")
  resp = st.checkbox("Estoy de acuerdo")
  resp_2 = st.checkbox("Por supuesto que sí")
  resp_3 = st.checkbox("NO")
  if resp:
    st.write("Correcto")
  if resp_2:
    st.write("<3")
  if resp_3:
    st.write("JJ. Jameson sé que eres tú -.-")
with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual","Auditiva", "Tactil"))
  if modo == "Visual":
    st.write("La vista es fundamental para ver cuantas telarañas debes lanzar")
  if modo == "Auditiva":
    st.write("La audicion es fundamental para saber cuanta gente hay basándote en las voces")
  if modo == "Tactil":
    st.write("El tacto es fundamental para derrotar a los malos (como a Scoprion...)")

st.subheader("Uso de Botones")
if st.button("Presiona el botón"):
      st.write("¿Presionarías todo lo que te dicen que toques? ¿y si fuera una bomba?")
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
