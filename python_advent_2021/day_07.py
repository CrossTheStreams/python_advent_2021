"""
Day 7 of Advent of Code 2021
"""

from typing import List
import re
from functools import cache

def median(nums: List[int]) -> int:
    """
    Calculate median
    """
    mid = len(nums)//2 - 1
    if len(nums) % 2 == 0:
        return sum(nums[mid:mid+2])//2
    return nums[mid]

def calculate_fuel_required_part_1(crab_positions: List[int]) -> int:
    """
    Calculate the lowest fuel cost possible, with the calculation required in Part 1.
    """
    med = median(crab_positions)
    diffs = list(map(lambda pos: abs(pos - med), crab_positions))
    return sum(diffs)

def day_07_part_1():
    """
    Day 7 Part 1
    """
    with open("inputs/day7.txt", encoding="utf-8") as f:
        crab_positions = [ int(val_str) for val_str in re.findall(r'\d+', f.read()) ]
        crab_positions.sort()
        fuel_required = calculate_fuel_required_part_1(crab_positions)
        print(f"Day 7 Part 1: Fuel required for the tiny crabs in submarines: 🦀 {fuel_required}")

def calculate_fuel_required_part_2(crab_positions: List[int]) -> int:
    """
    Calculate the lowest fuel cost possible, with the calculation required in Part 2.
    """
    @cache
    def count_steps(start_pos: int, end_pos: int) -> int:
        diff = abs(start_pos - end_pos)
        return sum(list(range(1, diff + 1)))

    @cache
    def calculate_cost_to(end_pos: int) -> int:
        return sum((count_steps(pos, end_pos) for pos in crab_positions))

    avg = round(sum(crab_positions)/len(crab_positions))
    current = avg
    cost = calculate_cost_to(end_pos=current)
    while True:
        left = current - 1
        left_fuel_cost = calculate_cost_to(end_pos=left)
        right = current + 1
        right_fuel_cost = calculate_cost_to(end_pos=right)
        if left_fuel_cost < cost:
            current = left
            cost = left_fuel_cost
            continue
        if right_fuel_cost < cost:
            current = right
            cost = right_fuel_cost
            continue
        break
    return cost

def day_07_part_2():
    """
    Day 7 Part 2
    """
    with open("inputs/day7.txt", encoding="utf-8") as f:
        crab_positions = [ int(val_str) for val_str in re.findall(r'\d+', f.read()) ]
        crab_positions.sort()
        fuel_required = calculate_fuel_required_part_2(crab_positions)
        print(f"Day 7 Part 2: Fuel required for the tiny crabs in submarines: 🦀 {fuel_required}")
