import streamlit as st

# Título del CV
st.title("LIZ VARGAS VIELMA")
st.header("Licenciatura en Administración y Finanzas")

# Crear columnas para la foto y la información personal
col1, col2 = st.columns([1, 2])  # Puedes ajustar las proporciones según lo necesites

# Columna 1: Foto
with col1:
    st.image("C:/Users/Liz/Documents/ClasePhyton/Mi_Primera_App_Streamlit/foto.jpg", caption="Tu Foto", width=150)

# Columna 2: Información Personal
with col2:
    st.header("Información Personal")
    st.markdown("""
    **Correo Electrónico:** 0239886@up.edu.mx  
    **Teléfono:** +52 33 21350387  
    **Ubicación:** Guadalajara, Jal  
    **Fecha de Nacimiento:** 05/11/2001
    """)
    
# Sobre mí
st.header("Sobre mí")
st.markdown("""
Tengo 22 años, estudiante del último semestre de mi licenciatura en Finanzas y Administración. Me defino como una persona con muchas ganas de aprender y dispuesta a afrontar retos. He trabajado en el área contable en una pequeña empresa y en el sector bancario en el área de crédito y negocios
""")

# Experiencia profesional
st.header("Experiencia Profesional")
st.markdown("""
### Asistente de Contabilidad
[PCML GROUP SC] | Enero 2021 - Abril 2021
- Registro de polizas de ingresos, gastos y diario de todas las operaciones contables de la empresa en el Sistema Contable.

###  Asistente de Negocios y Crédito
[BANSI BANCA MÚLTIPLE] | Diciembre 2022 - Diciembre 2023
-  Análisis Financiero de Estados Financieros.
-  Administración de inversiones.
-  Revisión de documentos para otorgar créditos.
-  Soporte en el área de Negocio de Banca Corporativa.
""")

# Educación
st.header("Educación")
st.markdown("""
Licenciatura en Administración y Finanzas
- Universidad Panamericana Campus Guadalajara | Agosto 2020 - Diciembre 2024

Intercambio de la Licenciatura en Administración y Finanzas
- Lyon 1 Claude Bernard, France | Enero 2024 - Mayo 2024

### Otros cursos y certificaciones
- Reconocimiento Académico: Durante mi carrera, fui reconocida por mantener uno de los mejores promedios entre los alumnos.
- Diploma en Educación Financiera CONDUSEF | Octubre - Diciembre 2021
- Certificación SAP Universidad Panamericana | Agosto 2023 - Diciembre 2023
- TOEFL IBT | Score 90 - Mayo 2023
            
""")

# Softwares
st.header("Softwares")
st.markdown("""
- CONTAPAQ I - Intermedio
- R STUDIO - Intermedio
- MICROSOFT OFFICE - Avanzado

""")

# Habilidades
st.header("Habilidades")
st.markdown("""
- Habilidades enfocadas a las matemáticas
- Conocimientos contables y financieros
- Flexible
- Organizada
- Proactiva
- Amable
- Creativa

""")

# Idiomas
st.header("Idiomas")
st.markdown("""
- Español - Nativo
- Inglés - Avanzado
- Frances - Intermedio

""")