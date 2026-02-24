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
# HELPERS
# -------------------------------------------------

def img_to_data_uri(path: Path | None) -> str | None:
    """Return a data URI for a local image (png/jpg)."""
    if not path or not Path(path).exists():
        return None

    p = Path(path)
    ext = p.suffix.lower().replace(".", "")
    if ext == "jpg":
        ext = "jpeg"

    data = p.read_bytes()
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:image/{ext};base64,{b64}"


def set_styles():
    # Background
    bg_path = Path("assets/backgrounds/stucco.png")
    bg_css = ""
    if bg_path.exists():
        encoded = base64.b64encode(bg_path.read_bytes()).decode()

        bg_css = f"""
        .stApp {{
            background-image:
                linear-gradient(rgba(250,244,228,0.88), rgba(250,244,228,0.88)),
                url("data:image/png;base64,{encoded}");
            background-size: 800px;
            background-repeat: repeat;
            background-attachment: fixed;
            background-position: top left;
        }}
        """

    css = f"""
    <style>
    {bg_css}

    /* Card container */
    .block-container {{
        background-color: rgba(255,248,235,0.95);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 0 40px rgba(0,0,0,0.15);
    }}

    /* ---- FORCE READABLE TEXT COLORS ---- */
    html, body, [class*="st-"], .stApp {{
        color: #2f2a23 !important;
    }}

    h1, h2, h3, h4, h5 {{
        color: #5a3b1e !important;
    }}

    .stMarkdown, .stText, p, li, span {{
        color: #2f2a23 !important;
    }}

    .stCaption, .stMarkdown small {{
        color: #6b5a44 !important;
        opacity: 1 !important;
    }}

    label, .stSelectbox label, .stDateInput label {{
        color: #2f2a23 !important;
    }}

    /* ---- CODEX GLYPH STRIP ---- */
    .codex-strip {{
        border: 5px solid #8b1e1e;
        border-radius: 6px;
        padding: 18px 14px;
        background-color: rgba(255,245,230,0.55);
        margin-top: 12px;
        margin-bottom: 18px;

        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 0px;
    }}

    .codex-cell {{
        padding: 8px 14px 10px 14px;
        text-align: center;
    }}

    .codex-cell + .codex-cell {{
        border-left: 3px solid #8b1e1e;
    }}

    .codex-title {{
        font-size: 0.95rem;
        color: #6b5a44 !important;
        margin-bottom: 10px;
    }}

    .codex-label {{
        font-weight: 600;
        margin-top: 10px;
        color: #2f2a23 !important;
    }}

    .codex-img {{
        width: 130px;
        height: auto;
        display: block;
        margin: 0 auto;
    }}

    .codex-stack {{
        display: flex;
        flex-direction: column;
        gap: 10px;
        align-items: center;
        justify-content: center;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


set_styles()

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
# GLYPH STRIP
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

num_uri = img_to_data_uri(Path(num_icon)) if num_icon else None
day_uri = img_to_data_uri(Path(day_icon)) if day_icon else None
yb_num_uri = img_to_data_uri(Path(yb_num_icon)) if yb_num_icon else None
yb_sign_uri = img_to_data_uri(Path(yb_sign_icon)) if yb_sign_icon else None

def img_html(uri: str | None) -> str:
    if not uri:
        return ""
    return f"<img class='codex-img' src='{uri}' />"

strip_html = f"""
<div class="codex-strip">
  <div class="codex-cell">
    <div class="codex-title">Número Tonal</div>
    {img_html(num_uri)}
    <div class="codex-label">{tonal_number if tonal_number else ""}</div>
  </div>

  <div class="codex-cell">
    <div class="codex-title">Signo del Día</div>
    {img_html(day_uri)}
    <div class="codex-label">{day_sign if day_sign else ""}</div>
  </div>

  <div class="codex-cell">
    <div class="codex-title">Portador del Año</div>
    <div class="codex-stack">
      {img_html(yb_num_uri)}
      {img_html(yb_sign_uri)}
    </div>
    <div class="codex-label">{year_bearer if year_bearer else ""}</div>
  </div>
</div>
"""

st.markdown(strip_html, unsafe_allow_html=True)

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

    # Red codex divider after "Día en Veintena"
    if label == "Día en Veintena":
        st.markdown("""
        <div style="
            border-top: 4px solid #8b1e1e;
            width: 85%;
            margin: 18px auto 18px auto;
            opacity: 0.9;
        "></div>
        """, unsafe_allow_html=True)