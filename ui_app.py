# ui_app.py
import streamlit as st
from datetime import date

from tonalpohualli.core import calculate_date

st.set_page_config(page_title="Tonalpohualli Diario", page_icon="🗿", layout="centered")

st.title("🗿 Tonalpohualli Diario")
st.caption("Lectura diaria estilo ‘horóscopo’ + búsqueda por fecha.")

# Sidebar controls
st.sidebar.header("Consulta")

today_clicked = st.sidebar.button("📅 Hoy")
if today_clicked:
    selected_date = date.today()
else:
    selected_date = st.sidebar.date_input("Elige una fecha", value=date.today())

# Calculate
result = calculate_date(selected_date)

# Display
st.subheader("Contexto Anual")
st.write(f"**Portador del Año:** {result.get('year_bearer', '—')}")
st.write(f"**Atadura de los Años:** {result.get('xiuhmolpilli_year', '—')} de 52")

st.divider()

st.subheader("Cuenta Diaria")
st.write(f"**Número Tonal:** {result.get('tonal_number', '—')}")
st.write(f"**Signo del Día:** {result.get('day_sign', '—')}")

# Nemontemi: show only what applies
if result.get("is_nemontemi") or result.get("day_sign") == "Nemontemi":
    st.info("Día Nemontemi: no aplican trecena/veintena/regencias diarias.")
    st.divider()
    st.subheader("Cierre")
    st.write(f"**Regente del Año:** {result.get('annual_regent_god', '—')}")
else:
    st.divider()

    st.subheader("Estructura Ritual")
    st.write(f"**Trecena:** {result.get('trecena', '—')}")
    st.write(f"**Regente de la Trecena:** {result.get('trecena_ruling_god', '—')}")

    st.write(f"**Veintena:** {result.get('veintena', '—')}")
    st.write(f"**Día en Veintena:** {result.get('dia_en_veintena', '—')}")
    st.write(f"**Regente de la Veintena:** {result.get('veintena_ruling_god', '—')}")

    st.divider()

    st.subheader("Regencias del Día")
    st.write(f"**Regente del Día:** {result.get('day_god', '—')}")
    st.write(f"**Señor de la Noche:** {result.get('lord_of_night', '—')}")

    st.divider()
    st.subheader("Cierre")
    # As requested: Regente del Año at the END
    st.write(f"**Regente del Año:** {result.get('annual_regent_god', '—')}")
