from datetime import date
from tonalpohualli.core import calculate_date

if __name__ == "__main__":
    today = date.today()
    result = calculate_date(today)
    print(result)
