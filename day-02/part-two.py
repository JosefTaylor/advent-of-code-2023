import os
import re

COLORS = ['red', 'green', 'blue']

def main():

    games = []


    with open('input.txt') as f:
        for line in f:
            parts = line.split(":")
            id = int(parts[0].split(' ')[1])
            game = { 'id':id, 'sets': []}
            for set_string in parts[1].split(';'):
                set = {}
                for color in COLORS:
                    m = re.search(f'(\d+) {color}', set_string)
                    set[color] = int(m.group(1)) if m else 0

                game['sets'].append(set)
            games.append(game)

    score = 0
    for game in games:
        score += power(min_set(game))

    print(score)


def min_set(game):
    min_set = {'red': 0, 'green': 0, 'blue': 0}
    for set in game['sets']:
        for color in COLORS:
            if set[color] > min_set[color]:
                min_set[color] = set[color]
    return min_set

def power(set):
    product = 1
    for color in COLORS:
        product = product * set[color]
    return product

main()