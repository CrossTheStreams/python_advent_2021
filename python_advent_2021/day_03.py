"""
Day 3 of Advent of Code 2021
"""
from collections import Counter
from typing import List

def calculate_power_consumption(bnumbers: List[str]) -> int:
    """
    Part 1
    Calculate the power consumption of the submarine, by calculating:
    gamma rate X epsilon rate
    """
    gamma: List[str] = []
    epsilon: List[str] = []
    for column in zip(*bnumbers):
        sorted_numbers = sorted(Counter(column).items(), key=lambda x: x[1], reverse=True)
        most_common = sorted_numbers[0][0]
        least_common = sorted_numbers[-1][0]
        gamma.append(most_common)
        epsilon.append(least_common)
    gamma_val = int("".join(gamma), 2)
    epsilon_val = int("".join(epsilon), 2)
    return gamma_val * epsilon_val

def calculate_life_support_rating(bnumbers: List[str]) -> int:
    """
    Part 2
    Calculate the life support rating:
    (oxygen generator) X (CO2 scrubber rating)
    """
    oxygen_rating = calculate_oxygen_rating(bnumbers)
    co2_scrubber_rating = calculate_co2_scrubber_rating(bnumbers)
    return oxygen_rating * co2_scrubber_rating

def calculate_oxygen_rating(bnumbers: List[str]) -> int:
    """
    Calculate the Oxygen Rating, a variable in the Life Support Rating
    """
    o_candidates = list(bnumbers)
    oxygen_digit = ''
    for idx in range(len(bnumbers[0])):
        column = [x[idx] for x in list(o_candidates)]
        number_counts = Counter(column)
        if number_counts['0'] > number_counts['1']:
            oxygen_digit = '0'
        else:
            oxygen_digit = '1'
        if len(o_candidates) == 1:
            break
        o_candidates = list(filter(lambda x, i=idx: x[i] == oxygen_digit, o_candidates))
    return int(o_candidates[0], 2)

def calculate_co2_scrubber_rating(bnumbers: List[str]) -> int:
    """
    Calculate the CO2 Scrubber Rating, a variable in the Life Support Rating
    """
    co2_candidates = list(bnumbers)
    co2_digit = ''
    for idx in range(len(bnumbers[0])):
        column = [x[idx] for x in list(co2_candidates)]
        number_counts = Counter(column)
        if number_counts['1'] < number_counts['0']:
            co2_digit = '1'
        else:
            co2_digit = '0'
        if len(co2_candidates) == 1:
            break
        co2_candidates = list(filter(lambda x, i=idx: x[i] == co2_digit, co2_candidates))
    co2_rating = int(co2_candidates[0], 2)
    return co2_rating

def _init_binary_nums() -> List[str]:
    with open("inputs/day3.txt", encoding="utf-8") as f:
        binary_nums = [binary_num.strip() for binary_num in f]
        return binary_nums

def day_03_part_1():
    """
    Day 3 Part 1
    """
    binary_nums = _init_binary_nums()
    print(f"Day 3 Part 1 Solution: {calculate_power_consumption(binary_nums)}")

def day_03_part_2():
    """
    Day 3 Part 2
    """
    binary_nums = _init_binary_nums()
    print(f"Day 3 Part 2 Solution: {calculate_life_support_rating(binary_nums)}")
