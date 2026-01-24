# Tonalpohualli Calendar Engine with Trecena Calculations - Latest Checkpoint

from datetime import date

# ---------------------------
# Constants: Day Signs, Lords, Gods, Roman Numerals
# ---------------------------
DAY_SIGNS = [
    "Cipactli", "Ehecatl", "Calli", "Cuetzpalin", "Coatl",
    "Miquiztli", "Mazatl", "Tochtli", "Atl", "Itzcuintli",
    "Ozomahtli", "Malinalli", "Acatl", "Ocelotl", "Cuauhtli",
    "Cozcacuauhtli", "Ollin", "Tecpatl", "Quiahuitl", "Xochitl"
]

LORDS_OF_NIGHT = [
    "Xiuhtecuhtli",
    "Itztli",
    "Piltzintecuhtli",
    "Centeotl",
    "Mictlantecuhtli",
    "Chalchiuhtlicue",
    "Tlazolteotl",
    "Tepeyollotl",
    "Tlaloc"
]

DAY_GODS = {
    "Cipactli": "Tonacatecuhtli",
    "Ehecatl": "Quetzalcoatl",
    "Calli": "Tepeyollotl",
    "Cuetzpalin": "Huehuecoyotl",
    "Coatl": "Chalchiuhtli",
    "Miquiztli": "Tecciztecatl",
    "Mazatl": "Tlaloc",
    "Tochtli": "Mayahuel",
    "Atl": "Xiuhtecuhtli",
    "Itzcuintli": "Mictlantecuhtli",
    "Ozomahtli": "Xochipili",
    "Malinalli": "Patecatl",
    "Acatl": "Tezcatlipoca",
    "Ocelotl": "Tlazolteotl",
    "Cuauhtli": "Xipe Totec",
    "Cozcacuauhtli": "Itzpapalotl",
    "Ollin": "Xolotl",
    "Tecpatl": "Chalchihuihtotolin",
    "Quiahuitl": "Tonatiuh",
    "Xochitl": "Xochiquetzal"
}

ROMAN_NUMERALS = ["I", "II", "III", "IV", "V", "VI"]

TRECENA_RULING_GODS = {
    "Cipactli": ["Tonacatecuhtli", "Tonacaccihuatl"],
    "Ocelotl": ["Quetzalcoatl"],
    "Mazatl": ["Tepeyollotl", "Quetzalcoatl", "Tlazolteotl"],
    "Xochitl": ["Huehuecoyotl", "Ixnextli"],
    "Acatl": ["Chalchihuitlicue", "Tlazolteotl"],
    "Miquiztli": ["Tonatiuh", "Tecciztecatl"],
    "Quiahuitl": ["Tlaloc", "Chicomecoatl"],
    "Malinalli": ["Mayahuel", "Xochipilli", "Cinteotl"],
    "Coatl": ["Xiuhtecuhtli", "Tlahuizcalpantecuhtli"],
    "Tecpatl": ["Mictlantecuhtli", "Tonatiuh"],
    "Ozomahtli": ["Patecatl"],
    "Cuetzpalin": ["Itzlacoliuhqui"],
    "Ollin": ["Tlazolteotl"],
    "Itzcuintli": ["Xipe Totec"],
    "Calli": ["Itzpapalotl"],
    "Cozcacuauhtli": ["Xolotl", "Tlalchitonatiuh"],
    "Atl": ["Chalchihuihtotolin"],
    "Ehecatl": ["Chantico"],
    "Cuauhtli": ["Xochiquetzal"],
    "Tochtli": ["Xiuhtecuhtli", "Itztapaltotec"]
}


# ---------------------------
# Anchor Date
# ---------------------------
ANCHOR_DATE = date(1506, 3, 13)      # March 13, 1506
ANCHOR_NUMBER = 1                     # Tonalpohualli number
ANCHOR_SIGN_INDEX = DAY_SIGNS.index("Cipactli")
ANCHOR_LORD_INDEX = LORDS_OF_NIGHT.index("Xiuhtecuhtli")

# ---------------------------
# Tonalpohualli Core Functions
# ---------------------------

def tonal_number(delta_days):
    return ((ANCHOR_NUMBER - 1 + delta_days) % 13) + 1

def day_sign(delta_days):
    index = (ANCHOR_SIGN_INDEX + delta_days) % 20
    return DAY_SIGNS[index]

def lord_of_night(delta_days):
    """
    Lords of Night cycle resets every 1 Cipactli (start of the 260-day tonalpohualli cycle).
    """
    # Find how many full 260-day cycles have passed
    cycle_offset = delta_days % 260

    # Determine the number of days since the last 1 Cipactli
    # 1 Cipactli is always delta = 0 in the cycle
    days_since_1_cipactli = cycle_offset

    # Lords of night cycle every 9 days
    index = days_since_1_cipactli % 9
    return LORDS_OF_NIGHT[index]


# ---------------------------
# Nemontemi-Adjusted Delta
# ---------------------------

def nemontemi_adjusted_delta(target_date):
    total_days = (target_date - ANCHOR_DATE).days
    years_since_anchor = 0
    days_remaining = total_days

    while True:
        year_length = 360 + 5  # 360 Tonalpohualli + 5 nemontemi

        # 6th nemontemi every 4 years, except every 128 years
        if (years_since_anchor + 1) % 4 == 0 and (years_since_anchor + 1) % 128 != 0:
            year_length += 1

        if days_remaining < year_length:
            break

        days_remaining -= year_length
        years_since_anchor += 1

    # Determine actual nemontemi length for this year
    nemontemi_length = 5
    if (years_since_anchor + 1) % 4 == 0 and (years_since_anchor + 1) % 128 != 0:
        nemontemi_length = 6

    # Check if target date is nemontemi
    if days_remaining >= 360:
        nemontemi_day_index = days_remaining - 360
        if nemontemi_day_index >= nemontemi_length:
            nemontemi_day_index = nemontemi_length - 1

        return {
            "is_nemontemi": True,
            "nemontemi_number": ROMAN_NUMERALS[nemontemi_day_index],
            "adjusted_delta": None
        }

    # Normal day: calculate delta skipping all previous nemontemi
    skipped_days = 0
    for y in range(years_since_anchor):
        skipped = 5
        if (y + 1) % 4 == 0 and (y + 1) % 128 != 0:
            skipped += 1
        skipped_days += skipped

    adjusted_delta = total_days - skipped_days
    return {"is_nemontemi": False, "adjusted_delta": adjusted_delta}

# ---------------------------
# Trecena Calculations (Anchor-aligned)
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
# Trecena Gods Formating Helper
# ---------------------------

def format_ruling_gods(gods_list):
    if not gods_list:
        return "None"
    if len(gods_list) == 1:
        return gods_list[0]
    return f"{gods_list[0]} ({', '.join(gods_list[1:])})"


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

# ---------------------------
# Helper function to print results nicely
# ---------------------------

def print_tonalpohualli(result):
    print(f"Gregorian Date: {result['gregorian_date']}")
    print(f"Tonal Number: {result['tonal_number']}")
    print(f"Day Sign: {result['day_sign']}")
    print(f"Day God: {result['day_god']}")
    print(f"Lord of Night: {result['lord_of_night']}")
    print(f"Trecena: {result['trecena']}")
    print(f"Trecena Ruling God: {result['trecena_ruling_god']}")
    print("-" * 40)

# ---------------------------
# Updated Test Block
# ---------------------------

if __name__ == "__main__":
    test_dates = [
        date(1506, 3, 13),
        date(1507, 3, 7),
        date(2026, 1, 23),
    ]

    for d in test_dates:
        result = calculate_date(d)
        print_tonalpohualli(result)
