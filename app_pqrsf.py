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
    opciones_tipo_paciente = ['Adulto', 'Pediatrico', 'Ambos']
    tipo_paciente_seleccionado = st.radio("Seleccione tipo de paciente", opciones_tipo_paciente)

    if 'Tipo de paciente' in df.columns:
        df['Tipo de paciente'] = df['Tipo de paciente'].astype(str).str.strip().str.lower()
        if tipo_paciente_seleccionado == 'Ambos':
            df_filtrado = df.copy()
        else:
            df_filtrado = df[df['Tipo de paciente'] == tipo_paciente_seleccionado.lower()].copy()
    else:
        st.warning("La columna 'Tipo de paciente' no se encontró en el archivo, no se aplicará filtro.")
        df_filtrado = df.copy()

    # --- FILTRO POR FECHAS ---
    if df_filtrado['Fecha creación'].notna().any():
        fecha_min = df_filtrado['Fecha creación'].min()
        fecha_max = df_filtrado['Fecha creación'].max()
    else:
        st.error("No hay fechas válidas en los datos.")
        st.stop()

    col1, col2 = st.columns(2)
    with col1:
        fecha_inicio = st.date_input("📅 Fecha de inicio", fecha_min)
    with col2:
        fecha_fin = st.date_input("📅 Fecha de fin", fecha_max)

    fecha_inicio = pd.to_datetime(fecha_inicio)
    fecha_fin = pd.to_datetime(fecha_fin)

    if fecha_inicio > fecha_fin:
        st.error("❌ La fecha de inicio debe ser anterior o igual a la fecha de fin.")
        st.stop()
    elif fecha_inicio < fecha_min or fecha_fin > fecha_max:
        st.error(f"❌ Las fechas deben estar dentro del rango: {fecha_min.date()} a {fecha_max.date()}.")
        st.stop()

    df_filtrado = df_filtrado[(df_filtrado['Fecha creación'] >= fecha_inicio) & (df_filtrado['Fecha creación'] <= fecha_fin)].copy()

    if df_filtrado.empty:
        st.warning("⚠️ No hay datos para ese rango de fechas.")
        st.stop()

    # --- FILTRO POR CONVENIO ---
    convenio_seleccionado = st.radio("Selecciona el tipo de convenio", ['Ambos', 'Segmento Privado', 'POS'])
    if convenio_seleccionado != 'Ambos':
        df_filtrado = df_filtrado[df_filtrado['Convenio.'].isin(convenios.get(convenio_seleccionado, []))].copy()

    # --- ANÁLISIS: Top 5 Quejas y Felicitaciones ---
    df_quejas = df_filtrado[df_filtrado['Tipo de requerimiento'].str.lower() == "queja"] if 'Tipo de requerimiento' in df_filtrado.columns else pd.DataFrame()
    df_felicitaciones = df_filtrado[df_filtrado['Tipo de requerimiento'].str.lower() == "felicitación"] if 'Tipo de requerimiento' in df_filtrado.columns else pd.DataFrame()

    st.subheader("📌 Top 5 Quejas y Felicitaciones")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🚨 Servicios con más Quejas")
        if not df_quejas.empty:
            st.table(df_quejas['Servicio afectado'].value_counts().head(5))
        else:
            st.info("No hay quejas para mostrar.")

        st.markdown("#### 🧑‍⚕️ Colaboradores con más Quejas")
        if 'Personal implicado' in df_quejas.columns and not df_quejas.empty:
            st.table(df_quejas['Personal implicado'].value_counts().head(5))
        else:
            st.info("No hay datos de 'Personal implicado' para quejas.")

    with col2:
        st.markdown("#### 🎉 Servicios con más Felicitaciones")
        if not df_felicitaciones.empty:
            st.table(df_felicitaciones['Servicio afectado'].value_counts().head(5))
        else:
            st.info("No hay felicitaciones para mostrar.")

        st.markdown("#### 👏 Colaboradores con más Felicitaciones")
        if 'Personal implicado' in df_felicitaciones.columns and not df_felicitaciones.empty:
            st.table(df_felicitaciones['Personal implicado'].value_counts().head(5))
        else:
            st.info("No hay datos de 'Personal implicado' para felicitaciones.")

    # --- GRÁFICO DE SOLICITUDES POR MES ---
    df_filtrado['Mes'] = df_filtrado['Fecha creación'].dt.to_period('M')
    conteo_mensual = df_filtrado['Mes'].value_counts().sort_index()

    st.markdown("### 📈 Gráfico de solicitudes por mes")
    fig, ax = plt.subplots(figsize=(10, 6))
    conteo_mensual.plot(kind='bar', ax=ax)
    ax.set_title('Cantidad de solicitudes por mes')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Número de solicitudes')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    st.pyplot(fig)

    # --- GRÁFICO POR SERVICIO AFECTADO ---
    servicios_buscados = st.multiselect(
        "Selecciona uno o varios Servicios Afectados para visualizar gráfico comparativo",
        options=df_filtrado['Servicio afectado'].dropna().unique()
    )

    if servicios_buscados:
        def servicio_en_fila(celda):
            if pd.isna(celda):
                return False
            servicios = []
            for sep in [';', ',']:
                servicios += [s.strip() for s in celda.split(sep)]
            servicios = list(set(servicios))
            return any(servicio in servicios for servicio in servicios_buscados)

        df_filtrado_servicios = df_filtrado[df_filtrado['Servicio afectado'].apply(servicio_en_fila)].copy()

        if df_filtrado_servicios.empty:
            st.warning("No se encontraron datos para los servicios seleccionados.")
        else:
            filas = []
            for _, row in df_filtrado_servicios.iterrows():
                tipos = row['Tipo de requerimiento']
                servicios_celda = []
                if pd.notna(row['Servicio afectado']):
                    for sep in [';', ',']:
                        servicios_celda += [s.strip() for s in str(row['Servicio afectado']).split(sep)]
                for servicio in servicios_celda:
                    filas.append({
                        'Tipo de requerimiento': tipos,
                        'Servicio afectado': servicio
                    })

            df_exp = pd.DataFrame(filas)
            tabla_pivot = pd.pivot_table(
                df_exp,
                index='Tipo de requerimiento',
                columns='Servicio afectado',
                aggfunc=len,
                fill_value=0
            )
            tabla_pivot = tabla_pivot.loc[:, [s for s in servicios_buscados if s in tabla_pivot.columns]]

            fig2, ax2 = plt.subplots(figsize=(10, 6))
            tabla_pivot.plot(kind="bar", ax=ax2)
            ax2.set_xlabel("Tipo de requerimiento")
            ax2.set_ylabel("Cantidad")
            ax2.set_title("Conteo por Tipo de Requerimiento y Servicio Afectado")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig2)

        # Mostrar tabla de personal implicado por servicio
        for servicio_buscado in servicios_buscados:
            df_servicio = df_filtrado[df_filtrado['Servicio afectado'].str.contains(servicio_buscado, case=False, na=False)].copy()
            if 'Personal implicado' in df_servicio.columns:
                df_servicio['Personal implicado'] = df_servicio['Personal implicado'].fillna('')
                servicio_personal_relacionado = df_servicio[['Servicio afectado', 'Personal implicado', 'Tipo de requerimiento']]
                st.subheader(f'Relación de Servicio Afectado con Personal Implicado para el servicio "{servicio_buscado}"')
                st.dataframe(servicio_personal_relacionado)
            else:
                st.info(f"No se encontró información de 'Personal implicado' para el servicio '{servicio_buscado}'.")

    # --- CONSULTA POR ESPECIALIDAD ---
    st.subheader("Consulta de solicitudes por especialidad")
    especialidad = st.selectbox("Selecciona una especialidad", list(especialidades.keys()))
    subespecialidades = actualizar_subespecialidades(especialidad)
    subespecialidad = st.selectbox("Selecciona una subespecialidad", subespecialidades)

    if 'Especialidad (Por tipo de solicitud Cita)' in df_filtrado.columns:
        df_filtrado['Especialidad (Por tipo de solicitud Cita)'] = df_filtrado['Especialidad (Por tipo de solicitud Cita)'].fillna('')
        df_especialidad = df_filtrado[df_filtrado['Especialidad (Por tipo de solicitud Cita)'].str.contains(especialidad, case=False)]
    else:
        df_especialidad = pd.DataFrame()
        st.warning("La columna 'Especialidad (Por tipo de solicitud Cita)' no se encontró en los datos.")

    tipos_requerimiento = ["petición", "queja", "reclamo", "felicitación", "sugerencia"]

    for tipo in tipos_requerimiento:
        df_tipo = df_especialidad[df_especialidad['Tipo de requerimiento'].str.lower() == tipo] if not df_especialidad.empty else pd.DataFrame()

        if df_tipo.empty:
            st.info(f"No hay {tipo}s registradas para la especialidad '{especialidad}'.")
        else:
            st.subheader(f'{tipo.capitalize()}s para la especialidad "{especialidad}"')
            st.dataframe(df_tipo)

    # --- CONSULTA DETALLADA DE QUEJAS POR CLASIFICACIÓN Y ESTADO ---
    st.subheader("Consulta detallada de Quejas por Clasificación y Estado")
    servicio_quejas = st.text_input("Ingrese el Servicio afectado para consulta detallada de quejas")

    if servicio_quejas:
        df_quejas = df_filtrado[df_filtrado['Tipo de requerimiento'].str.lower() == 'queja']
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
