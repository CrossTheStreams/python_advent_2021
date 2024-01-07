"""
Day 4 of Advent of Code 2021
"""

from typing import Dict, List, Tuple, Set
from collections import defaultdict
import re

class BingoBoard:
    """
    A bingo game to play on a submarine, as one does.
    """
    def __init__(self):
        self.board: List[List[int]] = []
        self.num_lookup: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        self.row_counts = [0 for i in range(5)]
        self.col_counts = [0 for i in range(5)]
        self.has_bingo = False
        self.last_number_called = None
        self.marked_coors: Set[Tuple[int, int]] = set([])

    def add_row(self, row):
        """
        Add a row to the board.
        """
        self.board.append(row)
        for col_idx, n in enumerate(row):
            row_idx = len(self.board) - 1
            self.num_lookup[n].append((row_idx, col_idx))

    def call_number(self, num: int):
        """
        Call a number in the Bingo game for this board.
        If this board has a winning number called, winning_score will return
        a non-zero score.
        """
        coors = self.num_lookup[num]
        for coor in coors:
            row_idx, col_idx = coor
            self.row_counts[row_idx] += 1
            if self.row_counts[row_idx] == 5:
                self.has_bingo = True
                self.last_number_called = num
            self.col_counts[col_idx] += 1
            if self.col_counts[col_idx] == 5:
                self.has_bingo = True
                self.last_number_called = num
            self.marked_coors.add(coor)

    @property
    def winning_score(self) -> int:
        """
        The winning score, if this board has won the Bingo game.
        Otherwise, this will return 0.
        """
        if self.has_bingo:
            unmarked_sum = 0
            unmarked_nums = []
            for row_idx in range(len(self.board[0])):
                for col_idx in range(len(self.board)):
                    if (row_idx, col_idx) not in self.marked_coors:
                        unmarked_nums.append(self.board[row_idx][col_idx])
                        unmarked_sum += self.board[row_idx][col_idx]
            return unmarked_sum * self.last_number_called
        return 0

def play_bingo(nums_to_call: int, bboards: List[BingoBoard]) -> int:
    """
    Play a game of bingo and return the winning score of the first
    board to win.
    """
    for num in nums_to_call:
        for bboard in bboards:
            bboard.call_number(num)
            if bboard.winning_score > 0:
                return bboard.winning_score

if __name__ == "__main__":
    with open("inputs/day4.txt", encoding="utf-8") as f:
        lines = [line for line in f]
        nums = list(map(int, re.findall(r'\d+', lines[0])))

        bingo_boards: List[BingoBoard] = []
        current_bboard = BingoBoard()
        for idx in range(1, len(lines)):
            line = lines[idx].strip()
            if line == "":
                if len(current_bboard.board) > 0:
                    bingo_boards.append(current_bboard)
                    current_bboard = BingoBoard()
                continue
            else:
                row = list(map(int, re.findall(r'\d+', line)))
                current_bboard.add_row(row)

        winning_score = play_bingo(nums, bingo_boards)
        print(f"Day 4, Part 1: Winning score for bingo game: {winning_score}")
