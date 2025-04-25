
import streamlit as st
import pandas as pd
import joblib
import re

@st.cache_resource
def cargar_modelo():
    return joblib.load("model.pkl")

modelo = cargar_modelo()
st.title("Predicción de Salario por Rol en el Sector IT")

with st.form("formulario"):
    st.subheader("Introduce los datos del perfil")

    anios = st.slider("Años de experiencia", 0, 50, 3)

    tamano = st.selectbox("Tamaño de empresa", [
        "Just me - I am a freelancer, sole proprietor, etc.",
        "2 to 9 employees", "10 to 19 employees", "20 to 99 employees",
        "100 to 499 employees", "500 to 999 employees",
        "1,000 to 4,999 employees", "5,000 to 9,999 employees",
        "10,000 or more employees"
    ])

    tipo_empleo = st.selectbox("Tipo de empleo", [
        "Jornada completa", "Media jornada", "Autónomo", "Estudiante", "Desempleado", "Jubilado", "Otro"
    ])

    trabajo_remoto = st.selectbox("Modalidad de trabajo", [
        "Remoto", "Presencial", "Híbrido"
    ])

    nivel_educativo = st.selectbox("Nivel educativo", [
        "Primaria", "Secundaria", "Grado medio", "Grado universitario", "Máster",
        "Doctorado", "Universidad sin título", "Otro"
    ])

    pais = st.selectbox("País", [
        "Alemania", "Australia", "Brasil", "Canadá", "España", "Estados Unidos de América",
        "Fancia", "India", "Italia", "Netherlands", "Polonia", "Reino Unido",
        "Suecia", "Suiza", "Otro"
    ])

    roles = st.multiselect("Rol profesional", [
        "Desarrollador Full Stack", "Desarrollador Back-End", "Desarrollador Front-End",
        "Desarrollador Mobile", "Desarrollador de Aplicaciones de Escritorio o Empresariales",
        "Desarrollador de Sistemas Embebidos", "Científico de Datos / Especialista en ML",
        "Especialista DevOps", "Manager de Ingeniería", "Otro"
    ])

    enviado = st.form_submit_button("Predecir")

if enviado:
    fila = {col: 0 for col in modelo.feature_names_in_}
    fila["anios_experiencia"] = anios
    fila["tamano_empresa"] = [
        "Just me - I am a freelancer, sole proprietor, etc.",
        "2 to 9 employees", "10 to 19 employees", "20 to 99 employees",
        "100 to 499 employees", "500 to 999 employees",
        "1,000 to 4,999 employees", "5,000 to 9,999 employees",
        "10,000 or more employees"
    ].index(tamano)

    fila[f"tipo_empleo_{tipo_empleo}"] = 1
    fila[f"trabajo_remoto_{trabajo_remoto}"] = 1
    fila[f"nivel_educativo_{nivel_educativo}"] = 1
    fila[f"pais_{pais}"] = 1

    for r in roles:
        clave = "rol_" + r
        if clave in fila:
            fila[clave] = 1

    df_pred = pd.DataFrame([fila])
    pred = modelo.predict(df_pred)[0]
    st.success(f"💰 Salario estimado: ${int(pred):,} USD")
