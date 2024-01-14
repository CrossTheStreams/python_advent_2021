"""
Day 5 of Advent of Code 2021
"""

from typing import List, Tuple
from collections import defaultdict
import re

Point = Tuple[int, int]
Line = Tuple[Point, Point]
LinePoints = List[Tuple[Point, Point]]

class VentMatrix:
    """
    A matrix of... vents!
    """
    def __init__(self):
        self.matrix = defaultdict(lambda: defaultdict(lambda: 0))

    def point(self, x, y) -> int:
        """
        A point in the matrix.
        """
        return self.matrix[x][y]

    def visit_point(self, x, y) -> int:
        """
        Mark a point in the matrix as visited.
        """
        self.matrix[x][y] += 1
        return self.point(x, y)

    def count_visited(self, visited_times: int) -> int:
        """
        Count the number of vents we've visited at least `visited_times` times.
        """
        count = 0
        for _x, y_coors in self.matrix.items():
            for _y, visit_count in y_coors.items():
                if visit_count >= visited_times:
                    count += 1
        return count

def setup_vent_lines(input_string: str) -> List[Line]:
    """
    Setup vent lines from input string.
    """
    vent_lines = []
    for line in input_string.split("\n"):
        nums = re.findall(r'\d+', line)
        point1 = tuple(map(int, nums[0:2]))
        point2 = tuple(map(int, nums[2:4]))
        vent_lines.append((point1, point2))
    return vent_lines

def horizontal_line_points(vent_lines: List[Line]) -> List[LinePoints]:
    """
    Get the points for horizontal lines.
    """
    lines = []
    line_points = list(filter(lambda vl: vl[0][0] == vl[1][0], vent_lines))
    for points in line_points:
        line = []
        x = points[0][0]
        y_coors = [points[0][1], points[1][1]]
        y_coors.sort()
        for y in range(y_coors[0], y_coors[1] + 1):
            line.append((x, y))
        lines.append(line)
    return lines

def vertical_line_points(vent_lines: List[Line]) -> List[LinePoints]:
    """
    Get the points for vertical lines.
    """
    lines = []
    line_points = list(filter(lambda vl: vl[0][1] == vl[1][1], vent_lines))
    for points in line_points:
        line = []
        y = points[0][1]
        x_coors = [points[0][0], points[1][0]]
        x_coors.sort()
        for x in range(x_coors[0], x_coors[1] + 1):
            line.append((x, y))
        lines.append(line)
    return lines

def day_05_part_1():
    """
    Day 5, Part 1
    """
    with open("inputs/day5.txt", encoding="utf-8") as f:
        input_string = f.read()
    vent_lines = setup_vent_lines(input_string)
    horizontal = horizontal_line_points(vent_lines)
    vertical = vertical_line_points(vent_lines)
    vent_matrix = VentMatrix()
    for points in horizontal:
        for point in points:
            x, y = point
            vent_matrix.visit_point(x, y)
    for points in vertical:
        for point in points:
            x, y = point
            vent_matrix.visit_point(x, y)
    count = vent_matrix.count_visited(visited_times=2)
    print(f"Day 5, Part 1: Count vents we've visited twice: {count}")

def day_05_part_2():
    """
    Day 5, Part 2
    """
    print("Day 5, Part 2: Up next! ☃️")
