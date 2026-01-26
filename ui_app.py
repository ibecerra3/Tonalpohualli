# ui_app.py

import streamlit as st
from datetime import date

from tonalpohualli.core import calculate_date


st.set_page_config(
    page_title="Tonalpohualli Diario",
    page_icon="🗿",
    layout="centered"
)

st.title("🗿 Tonalpohualli Diario")
st.caption("Lectura diaria estilo ‘horóscopo’ + búsqueda por fecha.")


# -------------------------
# Sidebar: Date Controls
# -------------------------
st.sidebar.header("Consulta")

if st.sidebar.button("📅 Hoy"):
    selected_date = date.today()
else:
    selected_date = st.sidebar.date_input(
        "Elige una fecha",
        value=date.today(),
        min_value=date(1400, 1, 1),
        max_value=date(2200, 12, 31),
    )


# -------------------------
# Calculate
# -------------------------
result = calculate_date(selected_date)


# -------------------------
# Render as a single list
# -------------------------
st.subheader("Lectura del Día")

aspects = []

# Annual context (top)
aspects.append(("Fecha Gregoriana", result.get("gregorian_date")))
aspects.append(("Portador del Año", result.get("year_bearer")))

xiuhmolpilli_year = result.get("xiuhmolpilli_year")
if xiuhmolpilli_year is not None:
    aspects.append(("Atadura de los Años", f"{xiuhmolpilli_year} de 52"))

# Daily core
aspects.append(("Número Tonal", result.get("tonal_number")))
aspects.append(("Signo del Día", result.get("day_sign")))

# Nemontemi handling
is_nemontemi = result.get("is_nemontemi") or result.get("day_sign") == "Nemontemi"
if is_nemontemi:
    aspects.append(("Estado", "Día Nemontemi — día de recogimiento"))
else:
    # Structure
    aspects.append(("Trecena", result.get("trecena")))
    aspects.append(("Regente de la Trecena", result.get("trecena_ruling_god")))

    aspects.append(("Veintena", result.get("veintena")))
    aspects.append(("Día en Veintena", result.get("dia_en_veintena")))
    aspects.append(("Regente de la Veintena", result.get("veintena_ruling_god")))

    # Daily regencies
    aspects.append(("Regente del Día", result.get("day_god")))
    aspects.append(("Señor de la Noche", result.get("lord_of_night")))

# Annual closure (always last)
aspects.append(("Regente del Año", result.get("annual_regent_god")))

# Print list
for label, value in aspects:
    if value is None:
        continue
    st.write(f"**{label}:** {value}")
