from datetime import date
from .constants import ANCHOR_DATE, ROMAN_NUMERALS

def nemontemi_adjusted_delta(target_date):
    total_days = (target_date - ANCHOR_DATE).days
    years_since_anchor = 0
    days_remaining = total_days

    while True:
        year_length = 360 + 5  # 360 Tonalpohualli + 5 nemontemi
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
        return {
            "is_nemontemi": True,
            "nemontemi_number": ROMAN_NUMERALS[nemontemi_day_index],
            "adjusted_delta": None
        }

    skipped_days = 0
    for y in range(years_since_anchor):
        skipped = 5
        if (y + 1) % 4 == 0 and (y + 1) % 128 != 0:
            skipped += 1
        skipped_days += skipped

    adjusted_delta = total_days - skipped_days
    return {"is_nemontemi": False, "adjusted_delta": adjusted_delta}
