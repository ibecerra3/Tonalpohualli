# ui_app.py

import streamlit as st
from datetime import datetime, date
from zoneinfo import ZoneInfo

from tonalpohualli.core import calculate_date

_ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}

def _nemontemi_label(result: dict) -> str:
    n = result.get("nemontemi_number")
    return f"Nemontemi {_ROMAN.get(n, '')}".strip()

def _is_blank(value) -> bool:
    """Hide placeholders that don't add value to the UI."""
    if value is None:
        return True
    if isinstance(value, str):
        v = value.strip()
        if v == "":
            return True
        if v.lower() in {"n/a", "na", "none", "ninguno", "nunguno", "unknown"}:
            return True
    return False


def _fmt(value):
    """User-friendly formatting for common types."""
    if isinstance(value, (list, tuple)):
        # Render lists as a clean comma-separated string
        return ", ".join(str(x) for x in value if not _is_blank(x))
    return value


st.set_page_config(
    page_title="Tonalpohualli Diario",
    page_icon="🌞",
    layout="centered",
)

st.title("🌞 Tonalpohualli Diario")
st.caption("Lectura diaria estilo ‘horóscopo’ + búsqueda por fecha.")

st.sidebar.header("Consulta")

# Timezone selector
timezone = st.sidebar.selectbox(
    "Zona horaria",
    ["America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles", "UTC"],
    index=0,
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
is_nemontemi = result.get("day_sign") == "Nemontemi" or result.get("is_nemontemi") is True

# Header row
left, right = st.columns([2, 1])
with left:
    st.subheader("Lectura del Día")
    st.write(f"**Fecha:** {selected_date.isoformat()}")
with right:
    st.write("\n")
    st.write(f"**Zona horaria:** {timezone}")

if is_nemontemi:
    st.info("Día **Nemontemi**: se ocultan campos de **Veintena** porque no aplican.")
else:
    st.caption("Trecena → Veintena → Regencias")

# --- Contexto anual ---
st.markdown("### Contexto anual")
ctx_items = [
    ("Portador del Año", result.get("year_bearer")),
    (
        "Atadura de los Años",
        f"{result['xiuhmolpilli_year']} de 52"
        if result.get("xiuhmolpilli_year") is not None
        else None,
    ),
    ("Regente del Año", result.get("annual_regent_god")),
]
for label, value in ctx_items:
    value = _fmt(value)
    if _is_blank(value):
        continue
    st.write(f"**{label}:** {value}")

# --- Núcleo tonal / diario ---
st.markdown("### Tonalpohualli")

if is_nemontemi:
    st.write(f"**Signo del Día:** {_nemontemi_label(result)}")
else:
    st.write(f"**Número Tonal:** {result.get('tonal_number')}")
    st.write(f"**Signo del Día:** {result.get('day_sign')}")


# --- Ciclos y regencias ---
st.markdown("### Ciclos y regencias")

if is_nemontemi:
    items = [
        ("Regente del Numeral", result.get("regente_del_numeral")),
        ("Volátil", result.get("volatil")),
    ]
else:
    items = [
        ("Trecena", result.get("trecena")),
        ("Veintena", result.get("veintena")),
        ("Día en Veintena", result.get("dia_en_veintena")),
        # Order requested: Numeral + Volátil before Regente del Día
        ("Regente del Numeral", result.get("regente_del_numeral")),
        ("Volátil", result.get("volatil")),
        ("Regente del Día", result.get("day_god")),
        ("Señor de la Noche", result.get("lord_of_night")),
        ("Regente de la Trecena", result.get("trecena_ruling_god")),
        ("Regente de la Veintena", result.get("veintena_ruling_god")),
    ]

for label, value in items:
    value = _fmt(value)
    if _is_blank(value):
        continue
    st.write(f"**{label}:** {value}")

with st.expander("Detalles técnicos", expanded=False):
    st.write("Estos campos ayudan a depurar cálculos (si los necesitas).")
    st.write(f"**Fecha Gregoriana (resultado):** {result.get('gregorian_date')}")
    if result.get("years_since_anchor") is not None:
        st.write(f"**Años desde ancla:** {result.get('years_since_anchor')}")
