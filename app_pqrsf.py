
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


# Diccionario de especialidades con sus subespecialidades
especialidades = {
    "Examenes Falla Cardiaca": [
        "Titulación", "Ecocardiograma", "Electrocardiogramas", "Pruebas de esfuerzo"
    ],
    "Examenes Gastroenterología": [
        "CEPRE", "Spyglas", "Cambios de botón", "Videocápsula", "Enteroscopia",
        "Colonoscopia", "Gastrostomía", "Endoscopia", "Extracción", "Mucosectomía",
        "Ligaduras", "Dilatación"
    ],
    "Examenes Cardio no Invasiva": [
        "Ecocardiogramas", "Pruebas de esfuerzo", "Ecocardiograma transesofágico",
        "Ecocardiograma estrés", "Perfusiones ambulatorias y hospitalizadas"
    ],
    "Anestesia": [],
    "Anticoagulación": [],
    "Cardiología": [],
    "Cirugía cardiovascular": [],
    "Cirugía de Torax": [],
    "Cirugía Gastrointestinal": [],
    "Cirugía General": [],
    "Cirugía Hepatobiliar": [],
    "Cirugía pediátrica": [],
    "Cirugía Plástica y Reconstructiva": [],
    "Clínica de heridas": [],
    "Dermatología": [],
    "Dolor y cuidados paliativos": [],
    "Electrofisiología": [],
    "Endocrinología": [],
    "Falla Cardiaca": [],
    "Fisiatría": [],
    "Gastroenterología": [],
    "Genética": [],
    "Geriatría": [],
    "Ginecología": [],
    "Hematología": [],
    "Hematoncológica": [],
    "Hemodinamia": [],
    "Hepatología": [],
    "Infectología": [],
    "Medicina Física y Rehabilitación": [],
    "Medicina Interna": [],
    "Medicina Nuclear": [],
    "Nefrología": [],
    "Neumología": [],
    "Neurocirugía": [],
    "Neurología": [],
    "Neuropsicología": [],
    "Neuroradiología": [],
    "Nutrición": [],
    "Oftalmología": [],
    "Oncología": [],
    "Optometría": [],
    "Ortopedía y Traumatología": [],
    "Otorrinolaringología": [],
    "Pediatría": [],
    "Psicología": [],
    "Psiquiatría": [],
    "Radiología": [],
    "Rehabilitación Cardiaca": [],
    "Reumatología": [],
    "Trasplante Hepático": [],
    "Trasplante Renal": [],
    "Trasplantes Cardíaco": [],
    "Trasplantes Pulmonar": [],
    "Urgencias General": [],
    "Urología": [],
    "Vascular Periférico": [],
    "Clínica de pared abdominal": [],
    "Neonatología": [],
    "Cl hepatitis viral": [],
    "Alergología": [],
    "Cl hepatocarcinoma": []
}

def actualizar_subespecialidades(especialidad):
    return especialidades.get(especialidad, [])

# Diccionario de convenios
convenios = {
    'Segmento Privado': ['Allianz', 'AXA Colpatria', 'COLMEDICA', 'COLSANITAS', 'COOMEVA MP','ECOPETROL S.A', 'MAPFRE COLOMBIA VIDA SEGUROS', 'MEDISANITAS', 'MEDPLUS MP', 'PAN AMERICAN LIFE', 'PARTICULAR', 'SEG.DE VIDA SURAMERICANA S.A', 'SEGUROS BOLIVAR', 'HDI SEGUROS COLOMBIA S.A', 'MUNCHENER RUCKVERSICHUNGS-GESELLSCHAFT AKTIENGESELLSCHAFT', 'ENNIA CARIBE SCHADE N.V.', 'PRESIDENCIA DE PANAMA', 'SZF STICHTING STAATSZIEKENFOND', 'USA MEDICAL SERVICES IHI BUPA', 'CIGNA INTERNACIONAL'],
    'POS': ['ALIANSALUD EPS', 'ASMET SALUD', 'SANITAS EPS','ASOCIACION MUTUAL SER', 'AXA COLPATRIA ARL', 'CAJA COPI', 'CAPITAL SALUD', 'COMPENSAR PLAN COMPLEMENTARIO', 'COMPENSAR POS, COOSALUD', 'FAMISANITAR EPS', 'FAMISANITAR PAC', 'MILITAR', 'NUEVA EPS', 'NUEVA EPS S.A PAC', 'NUEVA EPS S.A. REGIMEN SUBSIDIADO', 'POLICIA NACIONAL DIRECCIÓN DE SANIDAD', 'SALUD TOTAL E.P.S', 'SEGUROS BOLIVAR ARL', 'SEGUROS BOLIVAR POLIZA DE ACCIDENTES ESCOLARES', 'SURA EPS', 'UNIVERSIDAD DE NARIÑO', 'UNIVERSIDAD NACIONAL UNISALUD',  'U PEDAGOGICA Y TECNOLOG DE COL', 'FCI SOCIAL', 'FIDEICOMISOS PATRIMONIOS AUTONOMOS FIDUCIARIA', 'SEGUROS DE VIDA SURAMERICANA S.A. ARL', 'FAMISANITAR REGIMEN SUBSIDIADO', 'SALUD TOTAL REGIMEN SUBSIDIADO', 'EPS SURA REGIMEN SUBSIDIADO', 'FCI EMPLEADOS', 'COMPANIA MUNDIAL DE SEGUROS (ACCIDENTES DE TRANSITO)', 'REGIONAL DE ASEGURAMIENTO EN SALUD', 'SALUD TOTAL PAC',  'POSITIVA COMPAÑIA SEGUROS S.A', 'ADMINISTRADORA DE LOS RECURSOS DEL SISTEMA GENERAL DE SEGURIDAD SOCIAL EN SALUD', 'LA PREVISORA (ACCIDENTES DE TRANSITO)', 'SALUD BOLIVAR EPS', 'SEG.DE VIDA DEL ESTADO POL.JUV', 'ESTUDIOS DE INVESTIGACIÓN', 'SEGUROS COMERCIALES BOLIVAR S. (SOAT)', 'SEGUROS DEL ESTADO (SOAT)', 'ASEGURADORA SOLIDARIA COLOMBIA ENTIDAD COOPERATIVA', 'SEG.GENE.SURAMERICANA S.A (SOAT)', 'COLMENA A.R.L', 'DISPENSARIO MEDICO SUROCCIDENTE', 'POSITIVA COMPAÑIA SEGUROS S.A (ACCIDENTES ESCOLARES)','EPS FAMILIAR DE COLOMBIA S.A.S.', 'SEGUROS DE VIDA ALFA S.A. ARL', 'RIEGEL LTDA ASESORES DE SEGUROS', 'HDI SEGUROS COLOMBIA S.A (ACCIDENTES ESCOLARES)', 'FONDO FINANCIERO DISTRITAL DE SALUD', 'ALIANZA MEDELLIN ANTIOQUIA EPS S.A.S', 'AXA SEGUROS COLPATRIA S.A (SOAT)', 'ABBVIE S.A.S.', 'COMPENSAR SUBSIDIADO', 'ORGANIZACION INTERNACIONAL PARA LAS MIGRACIONES OIM', 'ALIANSALUD - REGIMEN SUBSIDIADO', 'SEG.VIDA SURAMERICANA POL JUVE', 'HDI SEGUROS COLOMBIA S.A (SOAT))']
}

def actualizar_subespecialidades(especialidad):
    return especialidades.get(especialidad, [])


st.title('📊 Análisis PQRSF')

uploaded_file = st.file_uploader("📁 Sube tu archivo Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.strip()
    df['Fecha creación'] = pd.to_datetime(df['Fecha creación'], errors='coerce')

    # --- FILTRO POR TIPO DE PACIENTE ---
    opciones_tipo_paciente = ['Adulto', 'Pediatrico']
    tipo_paciente_seleccionado = st.selectbox("Seleccione el tipo de paciente", opciones_tipo_paciente)

    if 'Tipo de paciente' in df.columns:
        df['Tipo de paciente'] = df['Tipo de paciente'].astype(str).str.strip().str.lower()
        tipo_paciente_filtrado = tipo_paciente_seleccionado.lower()
        df = df[df['Tipo de paciente'] == tipo_paciente_filtrado].copy()
    else:
        st.warning("La columna 'Tipo de paciente' no se encontró en el archivo, no se aplicará filtro.")
    # --- Selección de fechas primero ---
    col1, col2 = st.columns(2)
    with col1:
        fecha_inicio = st.date_input("📅 Fecha de inicio", datetime.today())
    with col2:
        fecha_fin = st.date_input("📅 Fecha de fin", datetime.today())

    fecha_inicio = pd.to_datetime(fecha_inicio)
    fecha_fin = pd.to_datetime(fecha_fin)

    fecha_min = df['Fecha creación'].min()
    fecha_max = df['Fecha creación'].max()

    if fecha_inicio > fecha_fin:
        st.error("❌ La fecha de inicio debe ser anterior o igual a la fecha de fin.")
        st.stop()
    elif fecha_inicio < fecha_min or fecha_fin > fecha_max:
        st.error(f"❌ Las fechas deben estar dentro del rango: {fecha_min.date()} a {fecha_max.date()}.")
        st.stop()

    # Filtrar datos por fecha
    df = df[(df['Fecha creación'] >= fecha_inicio) & (df['Fecha creación'] <= fecha_fin)].copy()

    if df.empty:
        st.warning("⚠️ No hay datos para ese rango de fechas.")
        st.stop()

    convenio_seleccionado = st.radio("Selecciona el tipo de convenio", ['Ambos', 'Segmento Privado', 'POS'])
    if convenio_seleccionado != 'Ambos':
        df_filtrado_convenio = df[df['Convenio.'].isin(convenios[convenio_seleccionado])]
    else:
        df_filtrado_convenio = df.copy()


    # Filtrar quejas y felicitaciones
    df_quejas = df[df['Tipo de requerimiento'].str.lower() == "queja"]
    df_felicitaciones = df[df['Tipo de requerimiento'].str.lower() == "felicitación"]

    # Top 5 Quejas y Felicitaciones
    st.subheader("📌 Top 5 Quejas y Felicitaciones")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🚨 Servicios con más Quejas")
        top_quejas_servicio = df_quejas['Servicio afectado'].value_counts().head(5)
        st.table(top_quejas_servicio)

        st.markdown("#### 🧑‍⚕️ Colaboradores con más Quejas")
        if 'Personal implicado' in df_quejas.columns:
            top_quejas_personal = df_quejas['Personal implicado'].value_counts().head(5)
            st.table(top_quejas_personal)
        else:
            st.info("No hay columna 'Personal implicado' en los datos.")

    with col2:
        st.markdown("#### 🎉 Servicios con más Felicitaciones")
        top_felicitaciones_servicio = df_felicitaciones['Servicio afectado'].value_counts().head(5)
        st.table(top_felicitaciones_servicio)

        st.markdown("#### 👏 Colaboradores con más Felicitaciones")
        if 'Personal implicado' in df_felicitaciones.columns:
            top_felicitaciones_personal = df_felicitaciones['Personal implicado'].value_counts().head(5)
            st.table(top_felicitaciones_personal)
        else:
            st.info("No hay columna 'Personal implicado' en los datos.")

    # Gráfico de solicitudes por mes
    df['Mes'] = df['Fecha creación'].dt.to_period('M')
    conteo_mensual = df['Mes'].value_counts().sort_index()

    st.markdown("### 📈 Gráfico de solicitudes por mes")
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 6))
    conteo_mensual.plot(kind='bar')
    plt.title('Cantidad de solicitudes por mes')
    plt.xlabel('Mes')
    plt.ylabel('Número de solicitudes')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    st.pyplot(plt)

    # Gráfico por servicio afectado
    servicio_buscado = st.text_input("Introduce el nombre del Servicio Afectado a visualizar (para gráfico)")

    if servicio_buscado:
        texto_busqueda = servicio_buscado.strip().lower()

        def servicio_en_fila(celda):
            if pd.isna(celda):
                return False
            servicios = []
            for sep in [';', ',']:
                servicios += [s.strip().lower() for s in celda.split(sep)]
            servicios = list(set(servicios))
            return any(texto_busqueda in s for s in servicios)

        df_servicio = df[df['Servicio afectado'].apply(servicio_en_fila)]

        if df_servicio.empty:
            st.warning(f"No se encontraron datos para el servicio '{servicio_buscado}'.")
        else:
            conteo_servicio = df_servicio['Tipo de requerimiento'].value_counts().sort_values(ascending=False)

            fig_serv, ax_serv = plt.subplots()
            bars = ax_serv.bar(conteo_servicio.index, conteo_servicio.values)
            ax_serv.set_title(f'Conteo de tipos de requerimiento para el servicio "{servicio_buscado}"')
            ax_serv.set_xlabel('Tipo de requerimiento')
            ax_serv.set_ylabel('Cantidad')

            for bar in bars:
                yval = bar.get_height()
                ax_serv.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center')

            st.pyplot(fig_serv)

            if 'Personal implicado' in df_servicio.columns:
                df_servicio['Personal implicado'] = df_servicio['Personal implicado'].fillna('')
                servicio_personal_relacionado = df_servicio[['Servicio afectado', 'Personal implicado', 'Tipo de requerimiento']]
                st.subheader(f'Relación de Servicio Afectado con Personal Implicado para el servicio "{servicio_buscado}"')
                st.dataframe(servicio_personal_relacionado)
            else:
                 st.info("No se encontró información de 'Personal implicado' para este servicio.")


    # Consulta de peticiones por especialidad
    st.subheader("Consulta de peticiones por especialidad")

    especialidad = st.selectbox("Selecciona una especialidad", list(especialidades.keys()))
    subespecialidades = actualizar_subespecialidades(especialidad)
    subespecialidad = st.selectbox("Selecciona una subespecialidad", subespecialidades)

    if 'Especialidad (Por tipo de solicitud Cita)' in df.columns:
        df['Especialidad (Por tipo de solicitud Cita)'] = df['Especialidad (Por tipo de solicitud Cita)'].fillna('')
        df_especialidad = df[df['Especialidad (Por tipo de solicitud Cita)'].str.contains(especialidad, case=False)]
    else:
        df_especialidad = pd.DataFrame()
        st.warning("La columna 'Especialidad (Por tipo de solicitud Cita)' no se encontró en los datos.")

    peticiones = df_especialidad[df_especialidad['Tipo de requerimiento'].str.lower() == "petición"] if not df_especialidad.empty else pd.DataFrame()

    if peticiones.empty:
        st.info(f"No hay peticiones registradas para la especialidad '{especialidad}'.")
    else:
        st.subheader(f'Peticiones para la especialidad "{especialidad}"')
        st.dataframe(peticiones)


    # Consulta detallada de Quejas por Clasificación y Estado
    st.subheader("Consulta detallada de Quejas por Clasificación y Estado")

    servicio_quejas = st.text_input("Ingrese el Servicio afectado para consulta detallada de quejas")

    if servicio_quejas:
        df_quejas = df[df['Tipo de requerimiento'].str.lower() == 'queja']
        df_filtrado_quejas = df_quejas[df_quejas['Servicio afectado'].str.lower() == servicio_quejas.lower()]

        if df_filtrado_quejas.empty:
            st.warning(f"No se encontraron quejas para el servicio afectado: {servicio_quejas}")
        else:
            clasificaciones = ['INSATISFACCIÓN', 'DÉFICIT EN EL PROCESO']
            resumen = []

            for clas in clasificaciones:
                df_clas = df_filtrado_quejas[df_filtrado_quejas['clasificación Queja'].str.upper() == clas]
                total = len(df_clas)
                solucionadas = df_clas[df_clas['Estado'].str.upper() == 'SOLUCIONADO'].shape[0]
                no_solucionadas = total - solucionadas

                resumen.append({
                    'Clasificación': clas,
                    'Total': total,
                    'Solucionadas': solucionadas,
                    'No solucionadas': no_solucionadas
                })

            resumen_df = pd.DataFrame(resumen)
            st.table(resumen_df)
