# tonalpohualli/helpers.py

def format_ruling_gods(gods_list):
    if not gods_list:
        return "Ninguno"
    if len(gods_list) == 1:
        return gods_list[0]
    return f"{gods_list[0]} ({', '.join(gods_list[1:])})"


def print_tonalpohualli(result):
    print(f"Fecha Gregoriana: {result['gregorian_date']}")

    # If it's a Nemontemi day, print ONLY Nemontemi info and exit
    if result.get("day_sign") == "Nemontemi":
        print(f"Día Nemontemi: {result.get('tonal_number', 'N/A')}")
        print("-" * 40)
        return

    # Normal Tonalpohualli day
    print(f"Número Tonal: {result['tonal_number']}")
    print(f"Signo del Día: {result['day_sign']}")
    print(f"Trecena: {result.get('trecena', 'N/A')}")
    print(f"Regente del Día: {result.get('day_god', 'N/A')}")
    print(f"Señor de la Noche: {result.get('lord_of_night', 'N/A')}")
    print(f"Regente de la Trecena: {result.get('trecena_ruling_god', 'N/A')}")
    print("-" * 40)
