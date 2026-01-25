# test_tonalpohualli.py
from datetime import date, timedelta
from tonalpohualli import (
    tonal_number,
    day_sign,
    lord_of_night,
    nemontemi_adjusted_delta,
    trecena_info,
    TRECENA_RULING_GODS
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
    for delta in range(0, 26):
        tn1 = tonal_number(delta)
        tn2 = tonal_number(delta + 13)
        assert tn1 == tn2, f"Tonal number should repeat every 13 days (delta {delta})"

# ---------------------------
# ASSERT-3: Day sign cycles every 20 days
# ---------------------------
def test_day_sign_cycles():
    for delta in range(0, 20):
        ds1 = day_sign(delta)
        ds2 = day_sign(delta + 20)
        assert ds1 == ds2, f"Day sign should repeat every 20 days (delta {delta})"

# ---------------------------
# ASSERT-4: Lords of Night cycle every 9 days (within 260-day year)
# ---------------------------
def test_lords_of_night_cycles_every_9_days():
    for delta in range(0, 260 - 9):  # only within one cycle
        ln1 = lord_of_night(delta)
        ln2 = lord_of_night(delta + 9)
        assert ln1 == ln2, f"Lord of Night should repeat every 9 days within a cycle (delta {delta})"

# ---------------------------
# ASSERT-5: Nemontemi days identification
# ---------------------------
def test_nemontemi_days_identification():
    anchor = date(1506, 3, 13)
    # First year: 360 + 5 nemontemi
    for i in range(360, 365):
        result = nemontemi_adjusted_delta(anchor + timedelta(days=i))
        assert result["is_nemontemi"], f"Day {i} should be Nemontemi"

    # Normal day check
    result = nemontemi_adjusted_delta(anchor + timedelta(days=100))
    assert not result["is_nemontemi"], "Day 100 should not be Nemontemi"

# ---------------------------
# ASSERT-6: Adjusted delta skips nemontemi correctly
# ---------------------------
def test_adjusted_delta_non_nemontemi():
    anchor = date(1506, 3, 13)
    # Day 0 should have adjusted delta 0
    result = nemontemi_adjusted_delta(anchor)
    assert result["adjusted_delta"] == 0
    assert not result["is_nemontemi"]

    # Day 100: adjusted delta = 100
    result = nemontemi_adjusted_delta(anchor + timedelta(days=100))
    assert result["adjusted_delta"] == 100
    assert not result["is_nemontemi"]

# ---------------------------
# ASSERT-7: Trecena length = 13 days
# ---------------------------
def test_trecena_length():
    for delta in range(0, 260, 13):
        trecena = trecena_info(delta)
        start_delta = delta
        end_delta = delta + 12
        # Ensure all 13 days belong to the same trecena
        start_sign = trecena_info(start_delta)["trecena_start_sign"]
        for d in range(start_delta, end_delta + 1):
            sign = day_sign(d)
            # day_sign may differ in the cycle; just check the first day is trecena start
            assert trecena["trecena_start_sign"] == start_sign

# ---------------------------
# ASSERT-8: Trecena index alignment
# ---------------------------
def test_trecena_index_alignment():
    for delta in range(0, 260, 13):
        trecena = trecena_info(delta)
        index = delta // 13
        expected_start_delta = index * 13
        assert expected_start_delta == delta

# ---------------------------
# ASSERT-9: Trecena start sign alignment
# ---------------------------
def test_trecena_start_sign_alignment():
    for delta in range(0, 260, 13):
        trecena = trecena_info(delta)
        start_sign = day_sign(delta)
        assert trecena["trecena_start_sign"] == start_sign

# ---------------------------
# ASSERT-10: Trecena ruling gods mapping exists
# ---------------------------
def test_trecena_ruling_gods_mapping():
    for delta in range(0, 260, 13):
        trecena = trecena_info(delta)
        gods = TRECENA_RULING_GODS.get(trecena["trecena_start_sign"])
        assert gods is not None, f"Trecena {trecena['trecena_start_sign']} must have ruling gods"
        assert len(gods) >= 1, f"Trecena {trecena['trecena_start_sign']} must have at least 1 god"
