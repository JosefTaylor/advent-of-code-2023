import os
import re

def main():
    digit_pattern = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
    score = 0

    with open('day-01.txt') as f:
    # with open('day-01.txt') as f:
        for line in f:
            i = 0
            numbers = []
            while (i < len(line)):
                m = re.search(digit_pattern, line[i:])
                if m:
                    i = i + 1 + line[i:].index(m.group(0))
                    numbers.append(worder(m.group(0)))
                else:
                    break
            print(numbers[0], numbers[-1])
            score += int(numbers[0] + numbers[-1])

    print(score)

def worder(m):
    digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    if m in digits.values():
        return m
    elif m in digits.keys():
        return digits[m]

main()