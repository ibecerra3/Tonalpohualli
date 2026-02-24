import streamlit as st
from datetime import datetime, date
from zoneinfo import ZoneInfo
import base64
from pathlib import Path

from tonalpohualli.core import calculate_date
from tonalpohualli.icons import (
    find_day_sign_icon,
    find_numeral_icon,
    parse_year_bearer,
)

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Tonalpohualli Diario",
    page_icon="🌞",
    layout="centered"
)

# -------------------------------------------------
# BACKGROUND (TILED STUCCO)
# -------------------------------------------------

def set_background():
    bg_path = Path("assets/backgrounds/stucco.png")

    if not bg_path.exists():
        return

    with open(bg_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: 
            linear-gradient(rgba(250,244,228,0.88), rgba(250,244,228,0.88)),
            url("data:image/png;base64,{encoded}");
        background-size: 800px;
        background-repeat: repeat;
        background-attachment: fixed;
        background-position: top left;
    }}

    .block-container {{
        background-color: rgba(255,248,235,0.95);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 0 40px rgba(0,0,0,0.15);
    }}

    h1, h2, h3 {{
        color: #5a3b1e;
    }}

    .stMarkdown {{
        color: #2f2a23;
    }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)

set_background()

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("🌞 Tonalpohualli Diario")
st.caption("Lectura diaria estilo códice.")

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header("Consulta")

timezone = st.sidebar.selectbox(
    "Zona horaria",
    ["America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles", "UTC"],
    index=0
)

today_local = datetime.now(ZoneInfo(timezone)).date()

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

# -------------------------------------------------
# GLYPH STRIP WITH CODEX FRAME
# -------------------------------------------------

st.subheader("Lectura del Día")

day_sign = result.get("day_sign")
tonal_number = result.get("tonal_number")
year_bearer = result.get("year_bearer")

num_icon = find_numeral_icon(tonal_number)
day_icon = find_day_sign_icon(day_sign)

yb_num, yb_sign = parse_year_bearer(year_bearer)
yb_sign_icon = find_day_sign_icon(yb_sign) if yb_sign else None
yb_num_icon = find_numeral_icon(yb_num) if yb_num else None

# --- Red Codex Frame Start ---
st.markdown("""
<div style="
    border: 6px solid #8b1e1e;
    padding: 25px 10px;
    border-radius: 6px;
    margin-bottom: 25px;
    background-color: rgba(255,245,230,0.6);
">
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")

def centered_column(title, icon1=None, icon2=None, label=None):
    st.markdown(
        f"<div style='text-align:center; font-size:0.95rem; color:#6b5a44; margin-bottom:8px;'>{title}</div>",
        unsafe_allow_html=True
    )

    if icon1:
        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
        st.image(str(icon1), width=130)
        st.markdown("</div>", unsafe_allow_html=True)

    if icon2:
        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
        st.image(str(icon2), width=130)
        st.markdown("</div>", unsafe_allow_html=True)

    if label:
        st.markdown(
            f"<div style='text-align:center; font-weight:600; margin-top:8px;'>{label}</div>",
            unsafe_allow_html=True
        )

with c1:
    centered_column(
        "Número Tonal",
        icon1=num_icon,
        label=str(tonal_number) if tonal_number else None
    )

with c2:
    centered_column(
        "Signo del Día",
        icon1=day_icon,
        label=day_sign
    )

with c3:
    centered_column(
        "Portador del Año",
        icon1=yb_num_icon,
        icon2=yb_sign_icon,
        label=year_bearer
    )

st.markdown("</div>", unsafe_allow_html=True)
# --- Red Codex Frame End ---

st.divider()

# -------------------------------------------------
# DETAILS
# -------------------------------------------------

aspects = []

aspects.append(("Fecha Gregoriana", result.get("gregorian_date")))
aspects.append(("Zona horaria", timezone))
aspects.append(("Portador del Año", year_bearer))

if result.get("xiuhmolpilli_year") is not None:
    aspects.append(("Atadura de los Años", f"{result['xiuhmolpilli_year']} de 52"))

aspects.append(("Número Tonal", tonal_number))
aspects.append(("Signo del Día", day_sign))

if not result.get("is_nemontemi"):
    aspects.append(("Trecena", result.get("trecena")))
    aspects.append(("Veintena", result.get("veintena")))
    aspects.append(("Día en Veintena", result.get("dia_en_veintena")))
    aspects.append(("Regente del Numeral", result.get("regente_del_numeral")))
    aspects.append(("Volátil", result.get("volatil")))
    aspects.append(("Regente del Día", result.get("day_god")))
    aspects.append(("Señor de la Noche", result.get("lord_of_night")))
    aspects.append(("Regente de la Trecena", result.get("trecena_ruling_god")))
    aspects.append(("Regente de la Veintena", result.get("veintena_ruling_god")))
    aspects.append(("Regente del Año", result.get("annual_regent_god")))

for label, value in aspects:
    if value is None:
        continue
    st.write(f"**{label}:** {value}")