# tonalpohualli/helpers.py

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
