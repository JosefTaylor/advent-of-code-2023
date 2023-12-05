import os
import re

def main():

    symbol_pattern = r'[\*\#\+\$=\-\/%&@]'
    number_pattern = r'\d'

    symbols = []
    numbers = []

    with open('input.txt') as f:
        for i, line in enumerate(f):
            searching = True
            for j, char in enumerate(line):
                if re.match(symbol_pattern, char):
                    symbols.append({'symbol':char, 'line':i, 'char':j})
                    searching = True
                elif re.match(number_pattern, char) and searching:
                    searching = False
                    numbers.append({'number':char, 'line':i, 'char':j})
                elif re.match(number_pattern, char):
                    numbers[-1]['number'] += char
                else:
                    searching = True

    sum_ratios = 0
    for symbol in symbols:
        if symbol['symbol'] == '*':
            adjacent_numbers = [number for number in numbers if is_adjacent(symbol, number)]
            if len(adjacent_numbers) == 2:
                sum_ratios  += int(adjacent_numbers[0]['number']) * int(adjacent_numbers[1]['number'])

    print(sum_ratios)

def is_adjacent(symbol, number):
    adjacent = abs(number['line'] - symbol['line']) <= 1 and symbol['char'] - number['char'] <= len(number['number']) and number['char'] - symbol['char'] <= 1
    return adjacent

main()