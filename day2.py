from itertools import cycle
from collections import Counter
import sys
import Levenshtein as lv

def prob1(s):
    twos = 0
    threes = 0
    for c in s:
        counter = set(Counter(c).values())
        if 2 in counter:
            twos += 1
        if 3 in counter:
            threes += 1
    return twos * threes

def prob2(s):
    for i, c in enumerate(s):
        for j in range(i+1, len(s)):
            dist = lv.distance(c, s[j])
            if dist == 1:
                out = "".join([c1 for c1, c2 in zip(c, s[j]) if c1 == c2])
                return out


if __name__ == "__main__":

    inp = sys.stdin.read().splitlines()
    print(prob1(inp))
    print(prob2(inp))