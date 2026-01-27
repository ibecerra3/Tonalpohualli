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

# -------------------------
# Sidebar: Timezone + Date Controls
# -------------------------
st.sidebar.header("Consulta")

# Timezone selector
timezone = st.sidebar.selectbox(
    "Zona horaria",
    [
        "America/New_York",
        "America/Chicago",
        "America/Denver",
        "America/Los_Angeles",
        "UTC",
    ],
    index=0
)

# Timezone-aware "today"
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

# -------------------------
# Calculate
# -------------------------
result = calculate_date(selected_date)

# -------------------------
# Render as a single list (same order as helpers.py)
# -------------------------
st.subheader("Lectura del Día")

aspects = []

# Fecha
aspects.append(("Fecha Gregoriana", result.get("gregorian_date")))
aspects.append(("Zona horaria", timezone))

# Contexto anual
aspects.append(("Portador del Año", result.get("year_bearer")))
if result.get("xiuhmolpilli_year") is not None:
    aspects.append(("Atadura de los Años", f"{result['xiuhmolpilli_year']} de 52"))

# Núcleo diario
aspects.append(("Número Tonal", result.get("tonal_number")))
aspects.append(("Signo del Día", result.get("day_sign")))

# Nemontemi handling
is_nemontemi = result.get("day_sign") == "Nemontemi" or result.get("is_nemontemi") is True
if is_nemontemi:
    if result.get("regente_del_numeral") is not None:
        aspects.append(("Regente del Numeral", result.get("regente_del_numeral")))

    # Regente del Año al final
    aspects.append(("Regente del Año", result.get("annual_regent_god")))

else:
    # Trecena
    aspects.append(("Trecena", result.get("trecena")))

    # Veintena
    aspects.append(("Veintena", result.get("veintena")))
    aspects.append(("Día en Veintena", result.get("dia_en_veintena")))

    # Regente del Numeral (after Día en Veintena)
    aspects.append(("Regente del Numeral", result.get("regente_del_numeral")))

    # Regencias diarias
    aspects.append(("Regente del Día", result.get("day_god")))
    aspects.append(("Señor de la Noche", result.get("lord_of_night")))

    # Regentes mayores
    aspects.append(("Regente de la Trecena", result.get("trecena_ruling_god")))
    aspects.append(("Regente de la Veintena", result.get("veintena_ruling_god")))

    # Regente del Año (always last)
    aspects.append(("Regente del Año", result.get("annual_regent_god")))

# Print list
for label, value in aspects:
    if value is None:
        continue
    st.write(f"**{label}:** {value}")
