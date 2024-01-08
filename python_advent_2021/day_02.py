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

def _init_moves() -> List[Dict[str, int]]:
    with open("inputs/day2.txt", encoding="utf-8") as f:
        moves = []
        for line in f:
            line = line.split(" ")
            direction = line[0]
            steps = line[1]
            moves.append({direction: steps})
        return moves

def day_02_part_1():
    """
    Day 2 Part 1
    """
    moves = _init_moves()
    print(f"Day 2, Part 1 solution: {calculate_position_part_1(moves)}")

def day_02_part_2():
    """
    Day 2 Part 2
    """
    moves = _init_moves()
    print(f"Day 2, Part 2 solution: {calculate_position_part_2(moves)}")
