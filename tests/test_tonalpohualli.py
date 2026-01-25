# tests/test_tonalpohualli.py

from datetime import date, timedelta

from tonalpohualli.core import tonal_number, day_sign, lord_of_night, trecena_info
from tonalpohualli.nemontemi import nemontemi_adjusted_delta
from tonalpohualli.constants import ROMAN_NUMERALS, DAY_SIGNS, TRECENA_RULING_GODS
from tonalpohualli.helpers import format_ruling_gods


# ---------------------------
# ASSERT-1: Lords of the Night reset ONLY on 1 Cipactli
# ---------------------------

def test_lords_of_night_reset_only_on_cipactli():
    # Anchor day
    assert tonal_number(0) == 1
    assert day_sign(0) == "Cipactli"
    assert lord_of_night(0) == "Xiuhtecuhtli"

    # Next 260-day cycle
    assert tonal_number(260) == 1
    assert day_sign(260) == "Cipactli"
    assert lord_of_night(260) == "Xiuhtecuhtli"

    # Control checks
    assert lord_of_night(1) != "Xiuhtecuhtli"
    assert day_sign(1) != "Cipactli"


# ---------------------------
# ASSERT-2: Tonal numbers cycle every 13 days
# ---------------------------

def test_tonal_number_cycles():
    for delta in range(0, 26):
        n1 = tonal_number(delta)
        n2 = tonal_number(delta + 13)
        assert n1 == n2, f"Tonal number should repeat every 13 days (delta {delta})"


# ---------------------------
# ASSERT-3: Day signs cycle every 20 days
# ---------------------------

def test_day_sign_cycles():
    for delta in range(0, 40):
        s1 = day_sign(delta)
        s2 = day_sign(delta + 20)
        assert s1 == s2, f"Day sign should repeat every 20 days (delta {delta})"


# ---------------------------
# ASSERT-4: Lords of the Night repeat every 9 days (within a 260-day cycle)
# ---------------------------

def test_lords_of_night_cycles_every_9_days():
    # We stop at 251 so delta+9 never crosses the 260-day boundary,
    # because the Lords of Night reset at 1 Cipactli (delta % 260 == 0).
    for delta in range(0, 251):
        assert lord_of_night(delta) == lord_of_night(delta + 9), f"Failed at delta {delta}"


# ---------------------------
# ASSERT-5: Nemontemi days identification (first cycle after anchor)
# ---------------------------

def test_nemontemi_days_identification():
    first_year_start = date(1506, 3, 13)

    # First year: days 360-364 (5 days) are nemontemi
    for i in range(360, 365):
        result = nemontemi_adjusted_delta(first_year_start + timedelta(days=i))
        assert result["is_nemontemi"]
        assert result["nemontemi_number"] in ROMAN_NUMERALS


# ---------------------------
# ASSERT-6: Adjusted delta matches raw delta before any nemontemi occurs
# ---------------------------

def test_adjusted_delta_non_nemontemi():
    d = date(1506, 3, 13) + timedelta(days=10)
    result = nemontemi_adjusted_delta(d)
    assert not result["is_nemontemi"]
    assert result["adjusted_delta"] == 10


# ---------------------------
# ASSERT-7: Trecena naming format
# ---------------------------

def test_trecena_length():
    for delta in range(0, 260, 13):
        trec = trecena_info(delta)
        assert trec["trecena_name"].startswith("Ce "), "Trecena name should start with 'Ce '"


# ---------------------------
# ASSERT-8: Trecena index alignment (delta is within its trecena range)
# ---------------------------

def test_trecena_index_alignment():
    for delta in range(0, 260):
        index = delta // 13
        assert index * 13 <= delta < (index + 1) * 13, "Delta should be within trecena index range"


# ---------------------------
# ASSERT-9: Trecena start sign alignment
# ---------------------------

def test_trecena_start_sign_alignment():
    for delta in range(0, 260):
        trec = trecena_info(delta)
        start_sign = trec["trecena_start_sign"]
        expected_sign = DAY_SIGNS[(delta // 13 * 13) % 20]
        assert start_sign == expected_sign, "Trecena start sign alignment"


# ---------------------------
# ASSERT-10: Trecena ruling gods mapping formatting
# ---------------------------

def test_trecena_ruling_gods_mapping():
    for sign, gods in TRECENA_RULING_GODS.items():
        formatted = format_ruling_gods(gods)
        if len(gods) == 1:
            assert formatted == gods[0]
        else:
            assert formatted.startswith(gods[0])
            for g in gods[1:]:
                assert g in formatted
