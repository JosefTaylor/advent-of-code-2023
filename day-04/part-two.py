import os
import re

def main():

    cards = []

    with open('input.txt') as f:
        for i, line in enumerate(f):
            card = {'quantity': 1, 'score': score(line)}
            cards.append(card)
        
    for i in range(len(cards)):
        start = i+1
        stop = min([start + cards[i]['score'], len(cards)])
        for j in range(start,stop):
            cards[j]['quantity'] += cards[i]['quantity']

    print( [card['quantity'] for card in cards])
    print(sum([card['quantity'] for card in cards]))


def score(line: str) -> int:
    line = line.split(":")[1]
    parts = line.split('|')
    winning = get_numbers(parts[0])
    having = get_numbers(parts[1])

    score = 0
    for have in having:
        if have in winning:
            score += 1

    return score


def get_numbers(line: str) -> list[int]:
    numbers = [int(num) for num in line.strip().split()]
    return numbers


main()