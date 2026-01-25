# tonalpohualli/xiuhpohualli.py

from tonalpohualli.constants import VEINTENAS, ROMAN_NUMERALS
from tonalpohualli.nemontemi import xiuhpohualli_year_context

def xiuhpohualli_info(target_date):
    """
    Returns a dict describing the xiuhpohualli position for a Gregorian date:
    - is_nemontemi: True/False
    - veintena: veintena name (or "Nemontemi")
    - day_in_veintena: 1..20 (or Roman I..VI if nemontemi)
    - veintena_index: 0..17 (or None if nemontemi)
    """
    ctx = xiuhpohualli_year_context(target_date)
    day_in_year = ctx["day_in_year"]

    # Nemontemi
    if ctx["is_nemontemi"]:
        idx = ctx["nemontemi_day_index"]
        return {
            "is_nemontemi": True,
            "veintena": "Nemontemi",
            "day_in_veintena": ROMAN_NUMERALS[idx],
            "veintena_index": None
        }

    # Regular 360-day portion: 18 veintenas * 20 days
    veintena_index = day_in_year // 20
    day_in_veintena = (day_in_year % 20) + 1

    return {
        "is_nemontemi": False,
        "veintena": VEINTENAS[veintena_index],
        "day_in_veintena": day_in_veintena,
        "veintena_index": veintena_index
    }
