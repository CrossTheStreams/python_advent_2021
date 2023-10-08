"""
Tests for Day 1 of Advent of Code 2021
"""

from python_advent_2021.day_01 import count_increasing_depths, count_increasing_sums

def test_part_one():
    """
    Test for Part 1
    """
    with open("inputs/day1.txt", encoding="utf-8") as f:
        depths = [int(line.strip()) for line in f]
        assert count_increasing_depths(depths) == 1532

def test_part_two():
    """
    Test for Part 2
    """
    with open("inputs/day1.txt", encoding="utf-8") as f:
        depths = [int(line.strip()) for line in f]
        assert count_increasing_sums(depths) == 1571
