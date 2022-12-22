import sys
from typing import Tuple, List

from helpers import helper


def calculate_totals(parsed_calories: List[list], limit: int = 1):
    group_sums = list([group[-1] for group in parsed_calories])
    total = max(group_sums)
    ind = group_sums.index(total)
    return ind, total


def run(input, limit: int = 1) -> Tuple:
    calorie_list = helper.parse_file(input)

    if not calorie_list:
        print("There are no calories to parse!", file=sys.stderr)

    # [[1,2,3,6], [4,4], [5,6,11]]
    parsed_calories = parse_calorie_list(calorie_list)

    elves, total_calories = [], 0
    for i in range(0, limit):
        elf, calories = calculate_totals(parsed_calories)
        elves.append(elf + 1)
        total_calories += calories
        parsed_calories[elf] = [-1]

    print(f"The elves are: {','.join(map(str, elves))} with the total calorie count of: {total_calories}")
    return elves, total_calories


def parse_calorie_list(calories: list) -> List[list]:
    calculated_calories = []
    tmp_group = []
    for ind, cal in enumerate(calories):
        # if the line is blank:
        # 1. sum up the group totals and make it the last index in the group list
        # 2. append the list to the calculated cals list
        # 3. clear the tmp group list
        if not cal.strip() or ind == len(calories) - 1:
            if ind == len(calories) - 1:
                tmp_group.append(int(cal))
            cal_sum = sum(tmp_group)
            tmp_group.append(cal_sum)
            calculated_calories.append(tmp_group)
            tmp_group = []
            continue

        # Add each call in the same section to the tmp list
        tmp_group.append(int(cal))

    return calculated_calories


if __name__ == '__main__':
    input_path = input("Enter the file path: ")
    top_num = input("How many calories do you want to get? (default: 1): ") or 1
    if isinstance(top_num, str):
        try:
            top_num = int(top_num)
        except ValueError:
            top_num = 1

    run(input_path, limit=top_num)
