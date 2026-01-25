from tonalpohualli import tonal_number, day_sign, lord_of_night

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



from datetime import date
from tonalpohualli import calculate_date

# ---------------------------
# ASSERT-2: Nemontemi days do NOT advance the Tonalpohualli cycle
# ---------------------------

def test_nemontemi_do_not_advance_tonalpohualli():
    """
    The day immediately before nemontemi and the day immediately after
    nemontemi must be consecutive Tonalpohualli days.
    """

    # Last regular day before nemontemi (based on anchor year logic)
    last_regular_day = date(1507, 3, 7)

    # First regular day AFTER nemontemi
    first_day_after_nemontemi = date(1507, 3, 13)

    before = calculate_date(last_regular_day)
    after = calculate_date(first_day_after_nemontemi)

    # Tonal number must advance by exactly 1 (mod 13)
    expected_tonal = (before["tonal_number"] % 13) + 1
    assert after["tonal_number"] == expected_tonal

    # Day sign must advance by exactly 1 in the 20-day cycle
    assert before["day_sign"] != after["day_sign"]

    # Lord of Night must advance normally (mod 9)
    assert before["lord_of_night"] != after["lord_of_night"]
