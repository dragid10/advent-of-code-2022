from typing import List


def parse_file(path: str) -> List:
    input = open(path).readlines()
    input = list(map(str.strip, input))
    return input
