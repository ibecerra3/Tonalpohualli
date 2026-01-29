# main.py

from datetime import date
from tonalpohualli.core import calculate_date
from tonalpohualli.helpers import print_tonalpohualli

if __name__ == "__main__":
    test_dates = [
        date(1506, 3, 13),
        date(1507, 3, 8),
        date(2026, 1, 29),
    ]

    for d in test_dates:
        result = calculate_date(d)
        print_tonalpohualli(result)
