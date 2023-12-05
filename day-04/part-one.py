import os
import re

def main():

    sum = 0

    with open('input.txt') as f:
        for line in f:
            sum += score(line)

    print(sum)


def score(line: str) -> int:
    line = line.split(":")[1]
    parts = line.split('|')
    winning = get_numbers(parts[0])
    having = get_numbers(parts[1])

    score = 0
    for have in having:
        if have in winning:
            score = score * 2 if score > 0 else 1

    return score


def get_numbers(line: str) -> list[int]:
    numbers = [int(num) for num in line.strip().split()]
    return numbers


main()