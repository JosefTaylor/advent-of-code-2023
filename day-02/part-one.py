import os
import re

COLORS = ['red', 'green', 'blue']
LIMIT = {'red': 12, 'green': 13, 'blue': 14}

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


    for game in games:
        game['possible'] = check_game(game)

    score = sum(game['id'] if game['possible'] else 0 for game in games)
    print(score)
                
def check_game(game):
    for set in game['sets']:
        for color in COLORS:
            if set[color] > LIMIT[color]:
                return False
    return True

main()