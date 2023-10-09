"""
Day 2 of Advent of Code 2021
"""

from typing import List, Dict

def calculate_position_part_1(moves: List[Dict[str, int]]) -> int:
    """
    Part 1
    Calculate the value of (horizontal position) X (the depth).
    """
    horizontal = 0
    depth = 0
    for move in moves:
        if move.get("forward"):
            horizontal += int(move["forward"])
        if move.get("down"):
            depth += int(move["down"])
        if move.get("up"):
            depth -= int(move["up"])
    return horizontal * depth

def calculate_position_part_2(moves: List[Dict[str, int]]) -> int:
    """
    Part 2
    Calculate the value of (horizontal position) X (the depth), now factoring in aim.
    """
    aim = 0
    depth = 0
    horizontal = 0
    for move in moves:
        if move.get("forward"):
            x = int(move["forward"])
            horizontal += x
            depth += (aim * x)
        if move.get("down"):
            aim += int(move["down"])
        if move.get('up'):
            aim -= int(move["up"])
    return horizontal * depth
