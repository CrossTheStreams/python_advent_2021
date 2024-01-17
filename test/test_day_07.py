from python_advent_2021.day_07 import (
    calculate_fuel_required_part_1,
    calculate_fuel_required_part_2
)

def test_calculate_fuel_required_part_1():
    """
    Test for part 1
    """
    crab_positions = sorted([16,1,2,0,4,2,7,1,2,14])
    assert 37 == calculate_fuel_required_part_1(crab_positions)

def test_calculate_fuel_required_part_2():
    """
    Test for part 2
    """
    crab_positions = sorted([16,1,2,0,4,2,7,1,2,14])
    assert 168 == calculate_fuel_required_part_2(crab_positions)
