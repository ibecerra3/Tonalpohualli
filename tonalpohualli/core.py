# tonalpohualli/core.py

from tonalpohualli.constants import (
    DAY_SIGNS, LORDS_OF_NIGHT, DAY_GODS, TRECENA_RULING_GODS
)
from tonalpohualli.nemontemi import nemontemi_adjusted_delta
from tonalpohualli.helpers import format_ruling_gods

# If you already have a different import for veintena info, keep YOUR import.
from tonalpohualli.xiuhpohualli import xiuhpohualli_info

# ---------------------------
# Tonalpohualli Core Functions
# ---------------------------

def tonal_number(delta_days, anchor_number=1):
    return ((anchor_number - 1 + delta_days) % 13) + 1

def day_sign(delta_days):
    return DAY_SIGNS[delta_days % 20]

def lord_of_night(delta_days):
    """
    Lords of Night cycle resets every 1 Cipactli (start of 260-day Tonalpohualli cycle).
    """
    cycle_offset = delta_days % 260
    index = cycle_offset % 9
    return LORDS_OF_NIGHT[index]

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
    result = nemontemi_adjusted_delta(target_date)

    if result["is_nemontemi"]:
        return {
            "gregorian_date": target_date.isoformat(),
            "tonal_number": result["nemontemi_number"],
            "day_sign": "Nemontemi",
            "day_god": None,
            "lord_of_night": None,
            "trecena": None,
            "trecena_ruling_god": None,
            # Veintena hidden during nemontemi:
            "veintena": None,
            "dia_en_veintena": None,
            "veintena_ruling_god": None,
            # Optional flag for helpers:
            "is_nemontemi": True
        }

    delta = result["adjusted_delta"]
    sign = day_sign(delta)

    # Trecena
    trecena = trecena_info(delta)
    ruling_gods_list = TRECENA_RULING_GODS.get(trecena["trecena_start_sign"])
    ruling_gods_display = format_ruling_gods(ruling_gods_list)

    # Veintena (Xiuhpohualli) — should return veintena, dia_en_veintena, veintena_ruling_god
    xiuh = xiuhpohualli_info(target_date)

    return {
        "gregorian_date": target_date.isoformat(),
        "tonal_number": tonal_number(delta),
        "day_sign": sign,
        "day_god": DAY_GODS.get(sign, "Unknown"),
        "lord_of_night": lord_of_night(delta),
        "trecena": trecena["trecena_name"],
        "trecena_ruling_god": ruling_gods_display,

        # Veintena output (after Trecena in helpers)
        "veintena": xiuh.get("veintena"),
        "dia_en_veintena": xiuh.get("dia_en_veintena"),
        "veintena_ruling_god": xiuh.get("veintena_ruling_god"),

        "is_nemontemi": False
    }
