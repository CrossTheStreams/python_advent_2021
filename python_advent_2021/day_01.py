"""
Day 1 of Advent of Code 2021
"""

from typing import List

def count_increasing_depths(depths: List[int]) -> int:
    """
    Part 1
    Count the number of increasing depths.
    """
    increases = 0
    current = depths[0]
    for depth in depths:
        if depth > current:
            current = depth
            increases += 1
        else:
            current = depth
    return increases

def count_increasing_sums(depths: List[int]) -> int:
    """
    Part 2
    Count the number of increasing sums of depths.
    """
    increases = 0
    current = sum(depths[0:3])
    for i in range(0, len(depths) - 2):
        depth_sum = sum(depths[i: i + 3])
        if depth_sum > current:
            current = depth_sum
            increases += 1
        else:
            current = depth_sum
    return increases
