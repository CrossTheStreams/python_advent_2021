"""
Tests for Day 3 of Advent of Code 2021
"""

from python_advent_2021.day_03 import (
    calculate_power_consumption,
    calculate_life_support_rating,
    calculate_oxygen_rating,
    calculate_co2_scrubber_rating
)

def test_part_one():
    """
    Test for Part 1
    """
    numbers = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]
    assert calculate_power_consumption(numbers) == 198

def test_part_two():
    """
    Test for Part 1
    """
    numbers = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]
    assert calculate_life_support_rating(numbers) == 230

def test_calculate_oxygen_rating():
    """
    Test for calculating Oxygen Rating
    """
    numbers = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]
    assert calculate_oxygen_rating(numbers) == 23

def test_calculate_co2_scrubber_rating():
    """
    Test for calculating CO2 Scrubber Rating
    """
    numbers = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]
    assert calculate_co2_scrubber_rating(numbers) == 10
