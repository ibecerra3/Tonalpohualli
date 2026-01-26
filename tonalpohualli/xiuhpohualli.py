# tonalpohualli/xiuhpohualli.py

from tonalpohualli.constants import VEINTENA_RULING_GODS
from tonalpohualli.helpers import format_ruling_gods
from tonalpohualli.nemontemi import xiuhpohualli_year_context


VEINTENAS = [
    "Atlcahualo",
    "Tlacaxipehualiztli",
    "Tozoztontli",
    "Huey Tozoztli",
    "Toxcatl",
    "Etzalcualiztli",
    "Tecuilhuitontli",
    "Huey Tecuilhuitl",
    "Tlaxochimaco (Miccailhuitontli)",
    "Xocotlhuetzi",
    "Ochpaniztli",
    "Teotleco",
    "Tepeilhuitl",
    "Quecholli",
    "Panquetzaliztli",
    "Atemoztli",
    "Tititl",
    "Izcalli",
]


def xiuhpohualli_info(target_date):
    """
    Returns veintena + day-in-veintena.
    Veintenas reset on the first day AFTER nemontemi.
    """

    ctx = xiuhpohualli_year_context(target_date)

    # During nemontemi, hide veintena
    if ctx["is_nemontemi"]:
        return {
            "veintena": None,
            "dia_en_veintena": None,
            "veintena_ruling_god": None
        }

    ritual_day_index = ctx["day_in_year"]  # 0–359 only

    veintena_index = ritual_day_index // 20
    dia_en_veintena = (ritual_day_index % 20) + 1

    veintena = VEINTENAS[veintena_index]

    # Lookup ruling gods
    ruling_gods_list = VEINTENA_RULING_GODS.get(veintena)
    veintena_ruling_god = format_ruling_gods(ruling_gods_list)

    return {
        "veintena": veintena,
        "dia_en_veintena": dia_en_veintena,
        "veintena_ruling_god": veintena_ruling_god
    }
