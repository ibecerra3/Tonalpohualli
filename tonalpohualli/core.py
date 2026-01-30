# tonalpohualli/core.py

from tonalpohualli.constants import (
    DAY_SIGNS,
    LORDS_OF_NIGHT,
    DAY_GODS,
    TRECENA_RULING_GODS,
    REGENTE_DEL_NUMERAL,
    VOLATIL_DEL_NUMERAL,
    YEAR_BEARER_SIGNS,
    ANCHOR_YEAR_BEARER_NUMBER,
    ANCHOR_YEAR_BEARER_SIGN,
    YEAR_REGENT_GODS,
)
from tonalpohualli.nemontemi import nemontemi_adjusted_delta, xiuhpohualli_year_context
from tonalpohualli.helpers import format_ruling_gods
from tonalpohualli.xiuhpohualli import xiuhpohualli_info


def tonal_number(delta_days, anchor_number=1):
    return ((anchor_number - 1 + delta_days) % 13) + 1


def day_sign(delta_days):
    return DAY_SIGNS[delta_days % 20]


def lord_of_night(delta_days):
    cycle_offset = delta_days % 260
    return LORDS_OF_NIGHT[cycle_offset % 9]


def year_bearer_info(years_since_anchor: int):
    try:
        anchor_sign_idx = YEAR_BEARER_SIGNS.index(ANCHOR_YEAR_BEARER_SIGN)
    except ValueError:
        anchor_sign_idx = 0

    sign = YEAR_BEARER_SIGNS[(anchor_sign_idx + years_since_anchor) % len(YEAR_BEARER_SIGNS)]
    number = ((ANCHOR_YEAR_BEARER_NUMBER - 1 + years_since_anchor) % 13) + 1
    year_name = f"{number} {sign}"

    regent = YEAR_REGENT_GODS[years_since_anchor % len(YEAR_REGENT_GODS)] if YEAR_REGENT_GODS else None
    xiuhmolpilli_year = (years_since_anchor % 52) + 1

    return {
        "year_bearer": year_name,
        "annual_regent_god": regent,
        "xiuhmolpilli_year": xiuhmolpilli_year,
        "years_since_anchor": years_since_anchor,
    }


def trecena_info(adjusted_delta):
    trecena_index = adjusted_delta // 13
    trecena_start_delta = trecena_index * 13
    trecena_start_sign = day_sign(trecena_start_delta)

    return {
        "trecena_name": f"Ce {trecena_start_sign}",
        "trecena_start_sign": trecena_start_sign,
    }


def calculate_date(target_date):
    # Annual context
    year_ctx = xiuhpohualli_year_context(target_date)
    year_meta = year_bearer_info(year_ctx["years_since_anchor"])

    # Tonalpohualli delta with nemontemi skipped
    result = nemontemi_adjusted_delta(target_date)

    # NEMONTEMI
    if result["is_nemontemi"]:
        nem_num = result["nemontemi_number"]
        return {
            "gregorian_date": target_date.isoformat(),

            "year_bearer": year_meta["year_bearer"],
            "xiuhmolpilli_year": year_meta["xiuhmolpilli_year"],
            "annual_regent_god": year_meta["annual_regent_god"],
            "years_since_anchor": year_meta["years_since_anchor"],

            # Nemontemi-specific (DO NOT return tonal_number / regente_del_numeral)
            "nemontemi_number": nem_num,
            "volatil": VOLATIL_DEL_NUMERAL.get(nem_num),

            "day_sign": "Nemontemi",
            "day_god": None,
            "lord_of_night": None,
            "trecena": None,
            "trecena_ruling_god": None,

            "veintena": None,
            "dia_en_veintena": None,
            "veintena_ruling_god": None,

            "is_nemontemi": True,
        }

    # NORMAL DAY
    delta = result["adjusted_delta"]
    sign = day_sign(delta)
    numeral = tonal_number(delta)

    trecena = trecena_info(delta)
    ruling_gods_list = TRECENA_RULING_GODS.get(trecena["trecena_start_sign"])
    ruling_gods_display = format_ruling_gods(ruling_gods_list)

    xiuh = xiuhpohualli_info(target_date)

    return {
        "gregorian_date": target_date.isoformat(),

        "year_bearer": year_meta["year_bearer"],
        "xiuhmolpilli_year": year_meta["xiuhmolpilli_year"],
        "annual_regent_god": year_meta["annual_regent_god"],
        "years_since_anchor": year_meta["years_since_anchor"],

        "tonal_number": numeral,
        "regente_del_numeral": REGENTE_DEL_NUMERAL.get(numeral, "Por definir"),
        "volatil": VOLATIL_DEL_NUMERAL.get(numeral),

        "day_sign": sign,
        "day_god": DAY_GODS.get(sign, "Unknown"),
        "lord_of_night": lord_of_night(delta),

        "trecena": trecena["trecena_name"],
        "trecena_ruling_god": ruling_gods_display,

        "veintena": xiuh.get("veintena"),
        "dia_en_veintena": xiuh.get("dia_en_veintena"),
        "veintena_ruling_god": xiuh.get("veintena_ruling_god"),

        "is_nemontemi": False,
    }
