# tonalpohualli/xiuhpohualli.py

from tonalpohualli.constants import VEINTENA_RULING_GODS
from tonalpohualli.helpers import format_ruling_gods


def xiuhpohualli_info(target_date):
    """
    This function should already exist in your project OR you should rename this
    to match the function you currently use.

    It must return:
      - veintena (str)
      - dia_en_veintena (int)
      - veintena_ruling_god (str)  <-- NEW
    """

    # ----------------------------------------------------------------
    # IMPORTANT:
    # Replace the next two lines with YOUR existing veintena calculation.
    # ----------------------------------------------------------------
    veintena = None
    dia_en_veintena = None
    # ----------------------------------------------------------------

    ruling_gods_list = VEINTENA_RULING_GODS.get(veintena)
    veintena_ruling_god = format_ruling_gods(ruling_gods_list)

    return {
        "veintena": veintena,
        "dia_en_veintena": dia_en_veintena,
        "veintena_ruling_god": veintena_ruling_god
    }
