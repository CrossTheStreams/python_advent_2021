"""
Day 6: Simulating Lanternfish
"""

from collections import defaultdict
import re
from typing import List

class LanternFishSchool:
    """
    A school of Lantern Fish
    """
    def __init__(self, first_generation: List[int]):
        self._school = defaultdict(lambda: 0)
        for num in first_generation:
            self._school[num] += 1

    def __len__(self) -> int:
        return sum(self._school.values())

    def tick(self):
        """
        Tick a day away for this school of LanternFish
        """
        new_vals = defaultdict(lambda: 0)
        for val in range(9):
            if val == 0:
                new_vals[8] = self._school[val]
                new_vals[6] = self._school[val]
            else:
                if val == 7:
                    new_vals[6] += self._school[val]
                else:
                    new_vals[val - 1] = self._school[val]
        self._school = new_vals

def day_06_part_1():
    """
    Day 6, Part 1
    """
    with open("inputs/day6.txt", encoding="utf-8") as f:
        input_string = f.read()
        first_gen = []
        for num_str in re.findall(r'\d+', input_string):
            first_gen.append(int(num_str))
        school = LanternFishSchool(first_generation=first_gen)
        for _ in range(80):
            school.tick()
        print(f"Day 6, Part 1: 80 days later, there are {len(school)} Lanternfish")

def day_06_part_2():
    """
    Day 6, Part 2
    """
    with open("inputs/day6.txt", encoding="utf-8") as f:
        input_string = f.read()
        first_gen = []
        for num_str in re.findall(r'\d+', input_string):
            first_gen.append(int(num_str))
        school = LanternFishSchool(first_generation=first_gen)
        for _ in range(256):
            school.tick()
        print(f"Day 6, Part 2: 256 days later, there are {len(school)} Lanternfish")
