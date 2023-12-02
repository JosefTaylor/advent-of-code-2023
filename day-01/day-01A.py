import os
import re

def main():
    digit_pattern = r'(\d)'
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
                    numbers.append(m.group(0))
                else:
                    break
            print(numbers[0], numbers[-1])
            score += int(numbers[0] + numbers[-1])

    print(score)

main()