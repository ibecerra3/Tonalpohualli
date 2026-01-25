# tonalpohualli/core.py

from .constants import (
    DAY_SIGNS, LORDS_OF_NIGHT, DAY_GODS, TRECENA_RULING_GODS
)
from .nemontemi import nemontemi_adjusted_delta
from .helpers import format_ruling_gods

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
            "day_god": "N/A",
            "lord_of_night": "N/A",
            "trecena": None,
            "trecena_ruling_god": None
        }

    delta = result["adjusted_delta"]
    sign = day_sign(delta)

    trecena = trecena_info(delta)
    ruling_gods_list = TRECENA_RULING_GODS.get(trecena["trecena_start_sign"])
    ruling_gods_display = format_ruling_gods(ruling_gods_list)

    return {
        "gregorian_date": target_date.isoformat(),
        "tonal_number": tonal_number(delta),
        "day_sign": sign,
        "day_god": DAY_GODS.get(sign, "Unknown"),
        "lord_of_night": lord_of_night(delta),
        "trecena": trecena["trecena_name"],
        "trecena_ruling_god": ruling_gods_display
    }
