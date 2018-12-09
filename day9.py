from itertools import cycle
import sys
from collections import defaultdict
from tqdm import tqdm
from blist import blist

def f(nplayer, last, debug=False):
    players = defaultdict(int)
    circle = blist([])
    current = None
    current_id = None
    for i, player in tqdm(zip(range(last+1), cycle(range(nplayer)))):
        if debug: print(circle, current, current_id)
        if not circle:
            circle.append(i)
            current = 0
            current_id = 0
            continue
        if circle == [0] and i == 1:
            circle.append(1)
            current = 1
            current_id = 1
            continue
        if i % 23 == 0:
            players[player] += i
            current = circle[current_id - 6]
            players[player] += circle.pop(current_id - 7)
            current_id = current_id - 7 if current_id - 7 >= 0 else (current_id - 6) % len(circle)
        else:
            new_id = (current_id + 2) % len(circle)
            if new_id == 0:
                circle.append(i)
                current_id = len(circle) - 1
            else:
                circle.insert(new_id, i)
                current_id = new_id
    return max(players.values())

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    players, point = map(int, [data[0], data[-2]])
    print(f(players, point))
    print(f(players, point * 100))