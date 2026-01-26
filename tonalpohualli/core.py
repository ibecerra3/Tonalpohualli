# tonalpohualli/core.py

from tonalpohualli.constants import (
    DAY_SIGNS,
    LORDS_OF_NIGHT,
    DAY_GODS,
    TRECENA_RULING_GODS,
    YEAR_BEARER_SIGNS,
    ANCHOR_YEAR_BEARER_NUMBER,
    ANCHOR_YEAR_BEARER_SIGN,
    YEAR_REGENT_GODS,
)
from tonalpohualli.nemontemi import nemontemi_adjusted_delta, xiuhpohualli_year_context
from tonalpohualli.helpers import format_ruling_gods

from tonalpohualli.xiuhpohualli import xiuhpohualli_info


# ---------------------------
# Tonalpohualli Core Functions
# ---------------------------

def tonal_number(delta_days, anchor_number=1):
    return ((anchor_number - 1 + delta_days) % 13) + 1


def day_sign(delta_days):
    return DAY_SIGNS[delta_days % 20]


def lord_of_night(delta_days):
    """Lords of Night cycle resets every 1 Cipactli (start of 260-day cycle)."""
    cycle_offset = delta_days % 260
    index = cycle_offset % 9
    return LORDS_OF_NIGHT[index]


# ---------------------------
# Year Bearers + Annual Regent Gods
# ---------------------------

def year_bearer_info(years_since_anchor: int):
    """Returns year bearer name (e.g., '1 Tochtli') and annual regent god."""
    if not YEAR_BEARER_SIGNS:
        year_name = None
    else:
        try:
            anchor_sign_idx = YEAR_BEARER_SIGNS.index(ANCHOR_YEAR_BEARER_SIGN)
        except ValueError:
            anchor_sign_idx = 0

        sign = YEAR_BEARER_SIGNS[(anchor_sign_idx + years_since_anchor) % len(YEAR_BEARER_SIGNS)]
        number = ((ANCHOR_YEAR_BEARER_NUMBER - 1 + years_since_anchor) % 13) + 1
        year_name = f"{number} {sign}"

    regent = None
    if YEAR_REGENT_GODS:
        regent = YEAR_REGENT_GODS[years_since_anchor % len(YEAR_REGENT_GODS)]

    return {
        "year_bearer": year_name,
        "annual_regent_god": regent,
        "years_since_anchor": years_since_anchor,
    }


# ---------------------------
# Trecena Calculations
# ---------------------------

def trecena_info(adjusted_delta):
    trecena_index = adjusted_delta // 13
    trecena_start_delta = trecena_index * 13
    trecena_start_sign = day_sign(trecena_start_delta)

    return {
        "trecena_name": f"Ce {trecena_start_sign}",
        "trecena_start_sign": trecena_start_sign,
    }


# ---------------------------
# Main Calculation Function
# ---------------------------

def calculate_date(target_date):
    # Solar-year context (xiuhpohualli) for year bearers and regent gods
    year_ctx = xiuhpohualli_year_context(target_date)
    year_meta = year_bearer_info(year_ctx["years_since_anchor"])

    # Tonalpohualli delta with nemontemi skipped
    result = nemontemi_adjusted_delta(target_date)

    if result["is_nemontemi"]:
        return {
            "gregorian_date": target_date.isoformat(),

            # Year context still applies during nemontemi
            "year_bearer": year_meta["year_bearer"],
            "annual_regent_god": year_meta["annual_regent_god"],
            "years_since_anchor": year_meta["years_since_anchor"],

            "tonal_number": result["nemontemi_number"],
            "day_sign": "Nemontemi",
            "day_god": None,
            "lord_of_night": None,
            "trecena": None,
            "trecena_ruling_god": None,

            # Veintena hidden during nemontemi
            "veintena": None,
            "dia_en_veintena": None,
            "veintena_ruling_god": None,

            "is_nemontemi": True,
        }

    delta = result["adjusted_delta"]
    sign = day_sign(delta)

    # Trecena
    trecena = trecena_info(delta)
    ruling_gods_list = TRECENA_RULING_GODS.get(trecena["trecena_start_sign"])
    ruling_gods_display = format_ruling_gods(ruling_gods_list)

    # Veintena (Xiuhpohualli)
    xiuh = xiuhpohualli_info(target_date)

    return {
        "gregorian_date": target_date.isoformat(),

        # Year context
        "year_bearer": year_meta["year_bearer"],
        "annual_regent_god": year_meta["annual_regent_god"],
        "years_since_anchor": year_meta["years_since_anchor"],

        # Tonalpohualli
        "tonal_number": tonal_number(delta),
        "day_sign": sign,
        "day_god": DAY_GODS.get(sign, "Unknown"),
        "lord_of_night": lord_of_night(delta),

        # Trecena
        "trecena": trecena["trecena_name"],
        "trecena_ruling_god": ruling_gods_display,

        # Veintena output
        "veintena": xiuh.get("veintena"),
        "dia_en_veintena": xiuh.get("dia_en_veintena"),
        "veintena_ruling_god": xiuh.get("veintena_ruling_god"),

        "is_nemontemi": False,
    }
