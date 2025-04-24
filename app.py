
import streamlit as st
import pandas as pd
import joblib
import re

@st.cache_resource
def cargar_modelo():
    return joblib.load("./src/models/model.pkl")

modelo = cargar_modelo()

st.title("💼 Predicción de Salario Anual en el Sector IT")

with st.form("formulario"):
    st.header("Introduce los datos del perfil")

    tipo_empleo = st.selectbox("Tipo de empleo", [
        "Full-time", "Part-time", "Freelancer", "Intern", "Other"
    ])

    trabajo_remoto = st.selectbox("Modalidad de trabajo", [
        "Remote", "Hybrid", "On-site"
    ])

    nivel_educativo = st.selectbox("Nivel educativo", [
        "Primary school", "Secondary school", "Professional certificate", "Associate degree",
        "Bachelor’s degree", "Master’s degree", "Doctorate"
    ])

    pais = st.selectbox("País de residencia", [
        "United States", "India", "Germany", "United Kingdom", "Canada",
        "France", "Brazil", "Spain", "Australia", "Netherlands",
        "Italy", "Poland", "Sweden", "Mexico", "Switzerland"
    ])

    experiencia = st.slider("Años de experiencia profesional", 0, 51, 3)
    
    tamano_empresa = st.selectbox("Tamaño de la empresa", [
        "Just me - I am a freelancer, sole proprietor, etc.",
        "2 to 9 employees", "10 to 19 employees", "20 to 99 employees",
        "100 to 499 employees", "500 to 999 employees",
        "1,000 to 4,999 employees", "5,000 to 9,999 employees",
        "10,000 or more employees"
    ])

    rol = st.multiselect("Rol/es dentro del sector", [
        "Developer, full-stack", "Developer, back-end", "Developer, front-end",
        "DevOps specialist", "Engineer, data", "Developer, mobile",
        "Data scientist or machine learning specialist", "Engineer, site reliability",
        "Data or business analyst", "Developer, embedded applications or devices",
        "Cloud infrastructure engineer", "Academic researcher", "Developer, game or graphics",
        "Engineer, security", "Product manager"
    ])

    enviado = st.form_submit_button("Predecir salario")

if enviado:
    columnas_modelo = modelo.feature_names_in_

    fila = {col: 0 for col in columnas_modelo}
    
    fila["Anios_experiencia"] = experiencia
    fila["Tamano_empresa"] = [
        "Just me - I am a freelancer, sole proprietor, etc.",
        "2 to 9 employees", "10 to 19 employees", "20 to 99 employees",
        "100 to 499 employees", "500 to 999 employees",
        "1,000 to 4,999 employees", "5,000 to 9,999 employees",
        "10,000 or more employees"
    ].index(tamano_empresa)

    fila[f"Pais_{pais}"] = 1
    fila[f"Tipo_empleo_{tipo_empleo}"] = 1
    fila[f"Trabajo_remoto_{trabajo_remoto}"] = 1
    fila[f"Nivel_educativo_{nivel_educativo}"] = 1

    for r in rol:
        nombre_col = re.sub(r"[^a-zA-Z0-9]", "_", r)
        if nombre_col in fila:
            fila[nombre_col] = 1

    df_pred = pd.DataFrame([fila])
    prediccion = modelo.predict(df_pred)[0]

    st.success(f"💰 El salario estimado es: ${int(prediccion):,} USD")
