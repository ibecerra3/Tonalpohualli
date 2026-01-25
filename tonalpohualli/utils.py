from .constants import DAY_GODS, TRECENA_RULING_GODS

def format_ruling_gods(gods_list):
    if not gods_list:
        return "None"
    if len(gods_list) == 1:
        return gods_list[0]
    return f"{gods_list[0]} ({', '.join(gods_list[1:])})"

def print_tonalpohualli(result):
    print(f"Gregorian Date: {result['gregorian_date']}")
    print(f"Tonal Number: {result['tonal_number']}")
    print(f"Day Sign: {result['day_sign']}")
    print(f"Day God: {result['day_god']}")
    print(f"Lord of Night: {result['lord_of_night']}")
    print(f"Trecena: {result['trecena']}")
    print(f"Trecena Ruling God: {result['trecena_ruling_god']}")
    print("-" * 40)

def calculate_date(delta, nemontemi_result, tonal_number_func, day_sign_func, lord_of_night_func, trecena_info_func):
    if nemontemi_result["is_nemontemi"]:
        return {
            "gregorian_date": None,
            "tonal_number": nemontemi_result["nemontemi_number"],
            "day_sign": "Nemontemi",
            "day_god": "None",
            "lord_of_night": "None",
            "trecena": None,
            "trecena_ruling_god": None
        }

    sign = day_sign_func(delta)
    trecena = trecena_info_func(delta)
    ruling_gods_list = TRECENA_RULING_GODS.get(trecena["trecena_start_sign"])
    ruling_gods_display = format_ruling_gods(ruling_gods_list)

    return {
        "gregorian_date": None,
        "tonal_number": tonal_number_func(delta),
        "day_sign": sign,
        "day_god": DAY_GODS.get(sign, "Unknown"),
        "lord_of_night": lord_of_night_func(delta),
        "trecena": trecena["trecena_name"],
        "trecena_ruling_god": ruling_gods_display
    }
