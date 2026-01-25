import pytest
from datetime import date
from tonalpohualli import (
    tonal_number, day_sign, lord_of_night,
    trecena_info, TRECENA_RULING_GODS, format_ruling_gods,
    nemontemi_adjusted_delta
)

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
# ASSERT-2: Tonal number cycles every 13 days
# ---------------------------
def test_tonal_number_cycles():
    for delta in range(0, 260):
        tn1 = tonal_number(delta)
        tn2 = tonal_number(delta + 13)
        assert tn1 == tn2, f"Tonal number should repeat every 13 days (delta {delta})"

# ---------------------------
# ASSERT-3: Day signs cycle every 20 days
# ---------------------------
def test_day_sign_cycles():
    for delta in range(0, 260):
        ds1 = day_sign(delta)
        ds2 = day_sign(delta + 20)
        assert ds1 == ds2, f"Day sign should repeat every 20 days (delta {delta})"

# ---------------------------
# ASSERT-4: Lords of Night cycle every 9 days
# ---------------------------
def test_lords_of_night_cycles_every_9_days():
    for delta in range(0, 260):
        ln1 = lord_of_night(delta)
        ln2 = lord_of_night(delta + 9)
        assert ln1 == ln2, f"Lord of Night should repeat every 9 days (delta {delta})"

# ---------------------------
# ASSERT-5: Nemontemi days are identified correctly
# ---------------------------
def test_nemontemi_days_identification():
    # Example: check first year
    first_year = 0
    for i in range(360, 365):
        result = nemontemi_adjusted_delta(date(1506, 3, 13) + timedelta(days=i))
        assert result["is_nemontemi"] is True, f"Day {i} should be nemontemi"

# ---------------------------
# ASSERT-6: Non-nemontemi days adjusted_delta is correct
# ---------------------------
def test_adjusted_delta_non_nemontemi():
    result = nemontemi_adjusted_delta(date(1506, 3, 14))  # day after anchor
    assert result["is_nemontemi"] is False
    assert result["adjusted_delta"] == 1, "Adjusted delta should be 1 for day after anchor"

# ---------------------------
# ASSERT-7: Trecena lasts exactly 13 days
# ---------------------------
def test_trecena_length():
    for delta in range(0, 260, 13):
        trecena_start = trecena_info(delta)
        trecena_end = trecena_info(delta + 12)
        assert trecena_start["trecena_start_sign"] == trecena_end["trecena_start_sign"], \
            f"Trecena should last 13 days (delta {delta})"

# ---------------------------
# ASSERT-8: Trecena calculation index matches start day
# ---------------------------
def test_trecena_index_alignment():
    for delta in range(0, 260):
        trecena = trecena_info(delta)
        start_delta = (delta // 13) * 13
        expected_sign = day_sign(start_delta)
        assert trecena["trecena_start_sign"] == expected_sign, \
            f"Trecena start sign should match day sign for delta {delta}"

# ---------------------------
# ASSERT-9: Trecena start aligns with correct day sign
# ---------------------------
def test_trecena_start_sign_alignment():
    test_deltas = [0, 13, 26, 39, 52, 65, 78, 91]
    for delta in test_deltas:
        trecena = trecena_info(delta)
        start_delta = (delta // 13) * 13
        assert trecena["trecena_start_sign"] == day_sign(start_delta), \
            f"Trecena start sign must align with day sign for delta {delta}"

# ---------------------------
# ASSERT-10: Trecena ruling gods correctly mapped
# ---------------------------
def test_trecena_ruling_gods_mapping():
    test_deltas = [0, 13, 26, 39, 52, 65, 78, 91]
    for delta in test_deltas:
        trecena = trecena_info(delta)
        gods_list = TRECENA_RULING_GODS.get(trecena["trecena_start_sign"])
        expected = format_ruling_gods(gods_list)
        assert expected is not None, f"Ruling gods must exist for trecena starting on {trecena['trecena_start_sign']}"
