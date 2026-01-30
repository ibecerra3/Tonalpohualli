# ui_app.py

import streamlit as st
from datetime import datetime, date
from zoneinfo import ZoneInfo

from tonalpohualli.core import calculate_date


st.set_page_config(
    page_title="Tonalpohualli Diario",
    page_icon="🌞",
    layout="centered"
)

st.title("🌞 Tonalpohualli Diario")
st.caption("Lectura diaria estilo ‘horóscopo’ + búsqueda por fecha.")

st.sidebar.header("Consulta")

# Timezone selector
timezone = st.sidebar.selectbox(
    "Zona horaria",
    ["America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles", "UTC"],
    index=0
)
today_local = datetime.now(ZoneInfo(timezone)).date()

# Date selection
if st.sidebar.button("📅 Hoy"):
    selected_date = today_local
else:
    selected_date = st.sidebar.date_input(
        "Elige una fecha",
        value=today_local,
        min_value=date(1400, 1, 1),
        max_value=date(2200, 12, 31),
    )

result = calculate_date(selected_date)

st.subheader("Lectura del Día")

aspects = []

# Fecha + contexto
aspects.append(("Fecha Gregoriana", result.get("gregorian_date")))
aspects.append(("Zona horaria", timezone))
aspects.append(("Portador del Año", result.get("year_bearer")))

if result.get("xiuhmolpilli_year") is not None:
    aspects.append(("Atadura de los Años", f"{result['xiuhmolpilli_year']} de 52"))

# Núcleo diario
aspects.append(("Número Tonal", result.get("tonal_number")))
aspects.append(("Signo del Día", result.get("day_sign")))

is_nemontemi = result.get("day_sign") == "Nemontemi" or result.get("is_nemontemi") is True
if is_nemontemi:
    aspects.append(("Regente del Numeral", result.get("regente_del_numeral")))
    aspects.append(("Volátil", result.get("volatil")))
    aspects.append(("Regente del Año", result.get("annual_regent_god")))
else:
    aspects.append(("Trecena", result.get("trecena")))

    aspects.append(("Veintena", result.get("veintena")))
    aspects.append(("Día en Veintena", result.get("dia_en_veintena")))

    # Regente del Numeral after Día en Veintena
    aspects.append(("Regente del Numeral", result.get("regente_del_numeral")))

    # ✅ Volátil immediately after Regente del Numeral
    aspects.append(("Volátil", result.get("volatil")))

    aspects.append(("Regente del Día", result.get("day_god")))
    aspects.append(("Señor de la Noche", result.get("lord_of_night")))

    aspects.append(("Regente de la Trecena", result.get("trecena_ruling_god")))
    aspects.append(("Regente de la Veintena", result.get("veintena_ruling_god")))

    # Always last
    aspects.append(("Regente del Año", result.get("annual_regent_god")))

for label, value in aspects:
    if value is None:
        continue
    st.write(f"**{label}:** {value}")
