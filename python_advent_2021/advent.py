"""
Entry point for running commands to solve AOC puzzles.
"""

import argparse

from python_advent_2021.day_01 import ( day_01_part_1, day_01_part_2 )
from python_advent_2021.day_02 import ( day_02_part_1, day_02_part_2 )
from python_advent_2021.day_03 import ( day_03_part_1, day_03_part_2 )
from python_advent_2021.day_04 import ( day_04_part_1, day_04_part_2 )
from python_advent_2021.day_05 import ( day_05_part_1, day_05_part_2 )
from python_advent_2021.day_06 import ( day_06_part_1, day_06_part_2 )
from python_advent_2021.day_07 import ( day_07_part_1, day_07_part_2 )

puzzles = {
    (1, 1): day_01_part_1,
    (1, 2): day_01_part_2,
    (2, 1): day_02_part_1,
    (2, 2): day_02_part_2,
    (3, 1): day_03_part_1,
    (3, 2): day_03_part_2,
    (4, 1): day_04_part_1,
    (4, 2): day_04_part_2,
    (5, 1): day_05_part_1,
    (5, 2): day_05_part_2,
    (6, 1): day_06_part_1,
    (6, 2): day_06_part_2,
    (7, 1): day_07_part_1,
    (7, 2): day_07_part_2,
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", required=True, type=int, choices=list(range(1, 26)))
    parser.add_argument("--part", required=True, type=int, choices=[1, 2])
    args = parser.parse_args()
    puzzle = puzzles.get((args.day, args.part))
    if puzzle:
        puzzle()
    else:
        print("Haven't done that one yet! 🐍☃️⛷️")
