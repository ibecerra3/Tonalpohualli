# tonalpohualli/helpers.py

def format_ruling_gods(gods_list):
    if not gods_list:
        return "Ninguno"
    if len(gods_list) == 1:
        return gods_list[0]
    return f"{gods_list[0]} ({', '.join(gods_list[1:])})"


def print_tonalpohualli(result):
    print(f"Fecha Gregoriana: {result['gregorian_date']}")
    print(f"Número Tonal: {result['tonal_number']}")
    print(f"Signo del Día: {result['day_sign']}")

    # Nemontemi: hide everything that doesn't apply
    if result.get("day_sign") == "Nemontemi" or result.get("is_nemontemi") is True:
        print("-" * 40)
        return

    # Normal days
    if result.get("trecena") is not None:
        print(f"Trecena: {result['trecena']}")

    # Veintena section (after Trecena)
    if result.get("veintena") is not None:
        print(f"Veintena: {result['veintena']}")
    if result.get("dia_en_veintena") is not None:
        print(f"Día en Veintena: {result['dia_en_veintena']}")

    # NEW ORDER — 13-cycle components FIRST
    if result.get("regente_del_numeral") is not None:
        print(f"Regente del Numeral: {result['regente_del_numeral']}")
    if result.get("volatil") is not None:
        print(f"Volátil: {result['volatil']}")

    # Then daily rulers
    if result.get("day_god") is not None:
        print(f"Regente del Día: {result['day_god']}")
    if result.get("lord_of_night") is not None:
        print(f"Señor de la Noche: {result['lord_of_night']}")

    if result.get("trecena_ruling_god") is not None:
        print(f"Regente de la Trecena: {result['trecena_ruling_god']}")

    if result.get("veintena_ruling_god") is not None:
        print(f"Regente de la Veintena: {result['veintena_ruling_god']}")

    print("-" * 40)
