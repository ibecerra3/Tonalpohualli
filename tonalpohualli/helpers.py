# tonalpohualli/helpers.py

def format_ruling_gods(gods_list):
    if not gods_list:
        return "Ninguno"
    if len(gods_list) == 1:
        return gods_list[0]
    return f"{gods_list[0]} ({', '.join(gods_list[1:])})"


def print_tonalpohualli(result):
    print(f"Fecha Gregoriana: {result['gregorian_date']}")

    # Nemontemi: ONLY show nemontemi label/number and hide everything else
    if result.get("day_sign") == "Nemontemi":
        print(f"Nemontemi: {result.get('tonal_number', 'N/A')}")
        print("-" * 40)
        return

    # Normal day output
    print(f"Número Tonal: {result.get('tonal_number', 'N/A')}")
    print(f"Signo del Día: {result.get('day_sign', 'N/A')}")
    print(f"Trecena: {result.get('trecena', 'N/A')}")

    # Xiuhpohualli / Veintena immediately after Trecena
    if result.get("veintena") is not None:
        print(f"Veintena: {result.get('veintena', 'N/A')}")
    if result.get("day_in_veintena") is not None:
        print(f"Día en Veintena: {result.get('day_in_veintena', 'N/A')}")

    print(f"Regente del Día: {result.get('day_god', 'N/A')}")
    print(f"Señor de la Noche: {result.get('lord_of_night', 'N/A')}")
    print(f"Regente de la Trecena: {result.get('trecena_ruling_god', 'N/A')}")
    print("-" * 40)
