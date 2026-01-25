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
