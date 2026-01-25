from datetime import date, timedelta
import pytest

from tonalpohualli.core import tonal_number, day_sign, lord_of_night
from tonalpohualli.nemontemi import nemontemi_adjusted_delta
from tonalpohualli.trecena import trecena_info
from tonalpohualli.constants import ROMAN_NUMERALS, DAY_SIGNS
from tonalpohualli.utils import format_ruling_gods

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
# ASSERT-4: Lords of the Night repeat every 9 days
# ---------------------------
def test_lords_of_night_cycles_every_9_days():
    for delta in range(0, 260):
        ln1 = lord_of_night(delta)
        ln2 = lord_of_night(delta + 9)
        # Wrap around the 260-day cycle
        delta_mod = (delta + 9) % 260
        ln2 = lord_of_night(delta_mod)
        assert ln1 == ln2, f"Lord of Night should repeat every 9 days (delta {delta})"

# ---------------------------
# ASSERT-5: Nemontemi days identification
# ---------------------------
def test_nemontemi_days_identification():
    # First year: days 360-364 are nemontemi (or 360-365 if leap nemontemi)
    first_year_start = date(1506, 3, 13)
    for i in range(360, 365):
        result = nemontemi_adjusted_delta(first_year_start + timedelta(days=i))
        assert result["is_nemontemi"], f"Day {i} should be Nemontemi"
        assert result["nemontemi_number"] in ROMAN_NUMERALS, f"Nemontemi number should be I-VI (day {i})"

# ---------------------------
# ASSERT-6: Adjusted delta skips nemontemi
# ---------------------------
def test_adjusted_delta_non_nemontemi():
    d = date(1506, 3, 13) + timedelta(days=10)  # within first tonalpohualli year
    result = nemontemi_adjusted_delta(d)
    assert not result["is_nemontemi"]
    assert result["adjusted_delta"] == 10

# ---------------------------
# ASSERT-7: Trecena length is 13
# ---------------------------
def test_trecena_length():
    for delta in range(0, 260, 13):
        trec = trecena_info(delta)
        assert trec["trecena_name"].startswith("Ce "), "Trecena name should start with 'Ce '"

# ---------------------------
# ASSERT-8: Trecena index alignment
# ---------------------------
def test_trecena_index_alignment():
    for delta in range(0, 260):
        trec = trecena_info(delta)
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
# ASSERT-10: Trecena ruling gods mapping
# ---------------------------
def test_trecena_ruling_gods_mapping():
    from tonalpohualli.constants import TRECENA_RULING_GODS
    for sign, gods in TRECENA_RULING_GODS.items():
        formatted = format_ruling_gods(gods)
        if len(gods) == 1:
            assert formatted == gods[0]
        else:
            assert gods[0] in formatted
            for g in gods[1:]:
                assert g in formatted

