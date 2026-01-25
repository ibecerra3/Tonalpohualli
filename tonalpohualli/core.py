# tonalpohualli/core.py

from datetime import date
from .constants import DAY_SIGNS, LORDS_OF_NIGHT, DAY_GODS, ROMAN_NUMERALS, TRECENA_RULING_GODS, ANCHOR_DATE, ANCHOR_NUMBER, ANCHOR_SIGN_INDEX
from .helpers import format_ruling_gods

# ---------------------------
# Tonalpohualli Core
# ---------------------------

def tonal_number(delta_days):
    return ((ANCHOR_NUMBER - 1 + delta_days) % 13) + 1

def day_sign(delta_days):
    index = (ANCHOR_SIGN_INDEX + delta_days) % 20
    return DAY_SIGNS[index]

def lord_of_night(delta_days):
    cycle_offset = delta_days % 260
    index = cycle_offset % 9
    return LORDS_OF_NIGHT[index]

def nemontemi_adjusted_delta(target_date):
    total_days = (target_date - ANCHOR_DATE).days
    years_since_anchor = 0
    days_remaining = total_days

    while True:
        year_length = 360 + 5
        if (years_since_anchor + 1) % 4 == 0 and (years_since_anchor + 1) % 128 != 0:
            year_length += 1
        if days_remaining < year_length:
            break
        days_remaining -= year_length
        years_since_anchor += 1

    nemontemi_length = 5
    if (years_since_anchor + 1) % 4 == 0 and (years_since_anchor + 1) % 128 != 0:
        nemontemi_length = 6

    if days_remaining >= 360:
        nemontemi_day_index = days_remaining - 360
        if nemontemi_day_index >= nemontemi_length:
            nemontemi_day_index = nemontemi_length - 1
        return {"is_nemontemi": True, "nemontemi_number": ROMAN_NUMERALS[nemontemi_day_index], "adjusted_delta": None}

    skipped_days = 0
    for y in range(years_since_anchor):
        skipped = 5
        if (y + 1) % 4 == 0 and (y + 1) % 128 != 0:
            skipped += 1
        skipped_days += skipped

    adjusted_delta = total_days - skipped_days
    return {"is_nemontemi": False, "adjusted_delta": adjusted_delta}

def trecena_info(adjusted_delta):
    trecena_index = adjusted_delta // 13
    trecena_start_delta = trecena_index * 13
    trecena_start_sign = day_sign(trecena_start_delta)
    return {"trecena_name": f"Ce {trecena_start_sign}", "trecena_start_sign": trecena_start_sign}

def calculate_date(target_date):
    result = nemontemi_adjusted_delta(target_date)
    if result["is_nemontemi"]:
        return {
            "gregorian_date": target_date.isoformat(),
            "tonal_number": result["nemontemi_number"],
            "day_sign": "Nemontemi",
            "day_god": "None",
            "lord_of_night": "None",
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
