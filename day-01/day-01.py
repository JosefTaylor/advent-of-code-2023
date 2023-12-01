import os
import re

def main():
    digit_pattern = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
    score = 0

    with open('test.txt') as f:
    # with open('day-01.txt') as f:
        for line in f:
            for (key, value) in digits:
                index = line.find(key)
                line = line[:index] + value + line[index:]
            line = re.sub(digit_pattern, "", line)
            number = int(line[0] + line[-1])
            print(number)
            score += number

    print(score)

def worder(m):
    digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    return (digits[m.group(0)] + m.group(0))

main()