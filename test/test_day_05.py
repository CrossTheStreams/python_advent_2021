import pytest
from python_advent_2021.day_05 import (
    diagonal_line_points,
    horizontal_line_points,
    setup_vent_lines,
    vertical_line_points,
    VentMatrix
)
INPUT_STRING = "\
0,9 -> 5,9\n\
8,0 -> 0,8\n\
9,4 -> 3,4\n\
2,2 -> 2,1\n\
7,0 -> 7,4\n\
6,4 -> 2,0\n\
0,9 -> 2,9\n\
3,4 -> 1,4\n\
0,0 -> 8,8\n\
5,5 -> 8,2"

def test_setup_vent_lines():
    vent_lines = setup_vent_lines(INPUT_STRING)
    assert vent_lines == [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((6, 4), (2, 0)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
        ((0, 0), (8, 8)),
        ((5, 5), (8, 2)),
    ]

def test_horizontal_line_points():
    """
    Test horizontal_line_points function
    """
    vent_lines = setup_vent_lines(INPUT_STRING)
    horizontal = horizontal_line_points(vent_lines)
    assert horizontal == [
        [(2, 1),(2, 2)],
        [(7, 0),(7, 1),(7, 2),(7, 3),(7, 4)]
    ]

def test_vertical_line_points():
    """
    Test vertical_line_points function
    """
    vent_lines = setup_vent_lines(INPUT_STRING)
    vertical = vertical_line_points(vent_lines)
    assert vertical == [
        [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)],
        [(3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4)],
        [(0, 9), (1, 9), (2, 9)],
        [(1, 4), (2, 4), (3, 4)],
    ]

def test_diagonal_line_points():
    """
    Test diagonal_line_points function
    """
    vent_lines = setup_vent_lines(INPUT_STRING)
    diagonal = diagonal_line_points(vent_lines)
    assert diagonal == [
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],
        [(2, 0), (3, 1), (4, 2), (5, 3), (6, 4)],
        [(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)],
        [(8, 2), (7, 3), (6, 4), (5, 5)]
    ]

def test_vent_matrix():
    """
    Test VentMatrix.
    """
    vent_lines = setup_vent_lines(INPUT_STRING)
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
    assert 5 == vent_matrix.count_visited(visited_times=2)
