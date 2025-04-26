import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cargar el modelo entrenado
model = joblib.load('./src/models/model.pkl')  # Asegúrate de tener este archivo

# Definir las variables esperadas
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

# Configurar la página
st.set_page_config(page_title="Predicción de Salario", page_icon="💰", layout="centered")
st.title("Predicción de salario por rol")

# Entradas del usuario
st.subheader("Introduce los datos del perfil")

anios_experiencia = st.number_input("Años de experiencia", min_value=0, max_value=50, value=5)

# Tamaño de la empresa
tamano_empresa = st.selectbox("Tamaño de la empresa", [
    '10-19_empleados', '+10000_empleados', '100-499_empleados', '20-99_empleados',
    '500-999_empleados', '1000-4999_empleados', '5000-9999_empleados'
])

# Rol principal
rol = st.selectbox("Rol principal", [
    'Developer_Full_Stack', 'Developer_Back_End', 'Developer_Front_End',
    'Developer_Desktop_Enterprise', 'Developer_Mobile', 'Developer_Embedded_Devices',
    'Data_Engineer', 'Engineering_Manager', 'DevOps_Specialist', 'Data_Scientist_ML',
    'Investigaci_n_Desarrollo', 'Investigador_Academico', 'Cloud_Infrastructure_Engineer',
    'Senior_Executive', 'Otro_rol'
])

# País
pais = st.selectbox("País", [
    'Australia', 'Brazil', 'Canada', 'France', 'Germany', 'India', 'Italy', 'Netherlands',
    'Poland', 'Spain', 'Sweden', 'Ukraine',
    'United_Kingdom_of_Great_Britain_and_Northern_Ireland', 'United_States_of_America','Otro'
])

# Modalidad de trabajo
modalidad = st.selectbox("Modalidad de trabajo", ['Autonomo', 'JornadaCompleta', 'MediaJornada'])

tipo_trabajo = st.selectbox("Tipo de trabajo", ['Hibrido', 'Presencial', 'Remoto'])

# Nivel educativo
nivel_educativo = st.selectbox("Nivel educativo", [
    'Doctorado', 'Grado_medio', 'Grado_universitario', 'Master',
    'Primaria', 'Secundaria', 'Universidad_sin_titulo', 'Otro_nivel_educativo'
])

# Botón para predecir
if st.button("Predecir salario"):
    # Crear un dataframe de una fila
    input_data = {var: 0 for var in variables}

    input_data['AniosExperiencia'] = anios_experiencia
    input_data['TamanoEmpresa'] = tamano_empresa
    input_data[rol] = 1
    input_data[pais] = 1
    input_data[modalidad] = 1
    input_data[tipo_trabajo] = 1
    input_data[nivel_educativo] = 1

    input_df = pd.DataFrame([input_data])

    # Predicción
    prediccion = model.predict(input_df)[0]

    st.success(f"El salario anual estimado es: {prediccion:,.2f} $")
