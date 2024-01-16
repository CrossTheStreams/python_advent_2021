from python_advent_2021.day_06 import (
    LanternFishSchool
)

def test_lanern_fish_school():
    """
    Test the LanternFish class
    """
    first_gen = [3, 4, 3, 1, 2]
    school = LanternFishSchool(first_generation=first_gen)
    assert len(school) == 5
    for _ in range(2):
        school.tick()
    assert len(school) == 6
    for _ in range(16):
        school.tick()
    assert len(school) == 26
    