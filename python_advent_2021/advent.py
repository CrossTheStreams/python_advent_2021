"""
Entry point for running commands to solve AOC puzzles.
"""

import argparse
from python_advent_2021.day_01 import (
    day_01_part_1,
    day_01_part_2
)
from python_advent_2021.day_02 import (
    day_02_part_1,
    day_02_part_2
)
from python_advent_2021.day_03 import (
    day_03_part_1,
    day_03_part_2
)
from python_advent_2021.day_04 import (
    day_04_part_1,
    day_04_part_2
)
from python_advent_2021.day_05 import (
    day_05_part_1,
    day_05_part_2
)

if __name__ == "__main__":    
    parser = argparse.ArgumentParser("day_04.py")
    parser.add_argument("--day", required=True, type=int, choices=list(range(1, 26)))
    parser.add_argument("--part", required=True, type=int, choices=[1, 2])
    args = parser.parse_args()
    match args.day:
        case 1:
            match args.part:
                case 1:
                    day_01_part_1()
                case 2:
                    day_01_part_2()
        case 2:
            match args.part:
                case 1:
                    day_02_part_1()
                case 2:
                    day_02_part_2()
        case 3:
            match args.part:
                case 1:
                    day_03_part_1()
                case 2:
                    day_03_part_2()
        case 4:
            match args.part:
                case 1:
                    day_04_part_1()
                case 2:
                    day_04_part_2()
        case 5:
            match args.part:
                case 1:
                    day_05_part_1()
                case 2:
                    day_05_part_2()
        case default:
            print("Haven't done that one yet! 🐍☃️⛷️")
