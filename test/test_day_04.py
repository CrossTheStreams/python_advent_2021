"""
Tests for Day 4 of Advent of Code 2021
"""
import re

from python_advent_2021.day_04 import (
    BingoBoard
)

def test_bingo_board_setup():
    """
    Adding rows works as expected.
    """
    row_strings = [
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        " 2  0 12  3  7",
    ]
    rows = [list(map(int, re.findall(r'\d+', row))) for row in row_strings]
    bboard = BingoBoard()
    for row in rows:
        bboard.add_row(row)

    assert bboard.board == [
        [14, 21, 17, 24,  4],
        [10, 16, 15,  9, 19],
        [18,  8, 23, 26, 20],
        [22, 11, 13,  6,  5],
        [ 2,  0, 12,  3,  7],
    ]


def test_bingo_board_win():
    """
    When we call winning numbers for the board,
    it's marked as a winner and we can score it.
    """
    row_strings = [
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        " 2  0 12  3  7",
    ]
    rows = [list(map(int, re.findall(r'\d+', row))) for row in row_strings]
    bboard = BingoBoard()
    for row in rows:
        bboard.add_row(row)

    for num in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21]:
        bboard.call_number(num)
        assert not bboard.has_bingo
        assert bboard.winning_score == 0

    bboard.call_number(24)
    assert bboard.has_bingo

    assert bboard.winning_score == 4512
