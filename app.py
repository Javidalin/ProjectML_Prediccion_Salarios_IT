import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Predicción de Salario", page_icon="💰", layout="centered")

@st.cache_resource
def cargar_modelo():
    return joblib.load("./src/models/model.pkl")  # contiene (modelo, columnas)

modelo, columnas = cargar_modelo()

variables = [
    'AniosExperiencia', 'TamanoEmpresa',
    'Developer_Full_Stack', 'Developer_Back_End', 'Otro_rol', 'Developer_Front_End',
    'Developer_Desktop_Enterprise', 'Developer_Mobile', 'Developer_Embedded_Devices',
    'Data_Engineer', 'Engineering_Manager', 'DevOps_Specialist', 'Data_Scientist_ML',
    'Investigaci_n_Desarrollo', 'Investigador_Academico', 'Cloud_Infrastructure_Engineer',
    'Senior_Executive', 'Australia', 'Brazil', 'Canada', 'France', 'Germany', 'India',
    'Italy', 'Netherlands', 'Otro', 'Poland', 'Spain', 'Sweden', 'Ukraine',
    'United_Kingdom_of_Great_Britain_and_Northern_Ireland', 'United_States_of_America',
    'Autonomo', 'JornadaCompleta', 'MediaJornada', 'Hibrido', 'Presencial', 'Remoto',
    'Doctorado', 'Grado_medio', 'Grado_universitario', 'Master', 'Otro_nivel_educativo',
    'Primaria', 'Secundaria', 'Universidad_sin_titulo'
]

st.title("Predicción de salario por perfil IT")

st.info("Completa el siguiente formulario para obtener una estimación de tu salario anual basado en tus características profesionales.")

# Inputs
st.subheader("Datos del perfil")

col1, col2 = st.columns(2)

with col1:
    anios_experiencia = st.number_input("Años de experiencia", min_value=0, max_value=50, value=5)
    tamano_empresa = st.selectbox("Tamaño de la empresa", [
    '10-19_empleados',
    '100-499_empleados',
    '1000-4999_empleados',
    '20-99_empleados',
    '500-999_empleados',
    '5000-9999_empleados',
    '+10000_empleados',
])
    modalidad = st.selectbox("Modalidad de trabajo", ['Autonomo', 'JornadaCompleta', 'MediaJornada'])

with col2:
    rol = st.selectbox("Rol principal", [
    'Cloud_Infrastructure_Engineer',
    'Data_Engineer',
    'Data_Scientist_ML',
    'Developer_Back_End',
    'Developer_Desktop_Enterprise',
    'Developer_Embedded_Devices',
    'Developer_Front_End',
    'Developer_Full_Stack',
    'Developer_Mobile',
    'DevOps_Specialist',
    'Engineering_Manager',
    'Investigaci_n_Desarrollo',
    'Investigador_Academico',
    'Senior_Executive',
    'Otro_rol'
])
    pais = st.selectbox("País", [
    'Australia',
    'Brazil',
    'Canada',
    'France',
    'Germany',
    'India',
    'Italy',
    'Netherlands',
    'Poland',
    'Spain',
    'Sweden',
    'Ukraine',
    'United_Kingdom_of_Great_Britain_and_Northern_Ireland',
    'United_States_of_America',
    'Otro'
    ])

    tipo_trabajo = st.selectbox("Tipo de trabajo", ['Presencial', 'Hibrido', 'Remoto'])

nivel_educativo = st.selectbox("Nivel educativo", [
    'Primaria',
    'Secundaria',
    'Grado_medio',
    'Universidad_sin_titulo',
    'Grado_universitario',
    'Master',
    'Doctorado',
    'Otro_nivel_educativo'
])

st.markdown("---")

# Predicción
if st.button("Predecir salario estimado"):
    input_data = {var: 0 for var in variables}

    input_data['AniosExperiencia'] = anios_experiencia
    input_data['TamanoEmpresa'] = tamano_empresa
    input_data[rol] = 1
    input_data[pais] = 1
    input_data[modalidad] = 1
    input_data[tipo_trabajo] = 1
    input_data[nivel_educativo] = 1

    input_df = pd.DataFrame([input_data])
    input_df = input_df[variables]

    prediccion = modelo.predict(input_df)[0]

    margen_inferior = prediccion * 0.85
    margen_superior = prediccion * 1.15

with st.container():
    st.subheader("Resultado de la estimación")

    st.success(f"El salario anual estimado es: {prediccion:,.2f} $. Puede variar entre {margen_inferior:,.2f} $ y {margen_superior:,.2f} $, dependiendo de factores externos.")

    st.caption("Recuerda que esta estimación depende de localización, experiencia real, demanda del mercado y políticas de empresa.")

with st.container():
    st.markdown("---")
    st.caption("🔹 API creada por Javier Vidal.")