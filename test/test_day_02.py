"""
Tests for Day 2 of Advent of Code 2021
"""

from python_advent_2021.day_02 import calculate_position_part_1, calculate_position_part_2

def test_part_one():
    """
    Test for Part 1
    """
    moves = [
        {"forward": 5},
        {"down": 5},
        {"forward": 8},
        {"up": 3},
        {"down": 8},
        {"forward": 2}
    ]
    assert calculate_position_part_1(moves) == 150

def test_part_two():
    """
    Test for Part 2
    """
    moves = [
        {"forward": 5},
        {"down": 5},
        {"forward": 8},
        {"up": 3},
        {"down": 8},
        {"forward": 2}
    ]
    assert calculate_position_part_2(moves) == 900
