from .constants import DAY_SIGNS, LORDS_OF_NIGHT, ANCHOR_NUMBER, ANCHOR_SIGN_INDEX

def tonal_number(delta_days):
    return ((ANCHOR_NUMBER - 1 + delta_days) % 13) + 1

def day_sign(delta_days):
    index = (ANCHOR_SIGN_INDEX + delta_days) % 20
    return DAY_SIGNS[index]

def lord_of_night(delta_days):
    """
    Lords of Night cycle resets every 1 Cipactli (start of the 260-day tonalpohualli cycle).
    """
    cycle_offset = delta_days % 260
    days_since_1_cipactli = cycle_offset
    index = days_since_1_cipactli % 9
    return LORDS_OF_NIGHT[index]
