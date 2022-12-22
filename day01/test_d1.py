from day01 import d1


def test_day01_pt1():
    sample_calorie_file = "inputs/sample.txt"

    # Expected results
    expected_elf = 4
    expected_calories = 24000

    # Actual results
    actual_elf, actual_calories = d1.run(sample_calorie_file)

    assert expected_elf == actual_elf
    assert expected_calories == expected_calories
