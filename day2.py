from itertools import combinations
from collections import Counter
import sys
# import Levenshtein as lv

def _cmp(a, b):
    return sum(m != n for m,n in zip(a, b))

def prob1(s):
    counters = [set(Counter(c).values()) for c in s]
    twos = sum(2 in k for k in counters)
    threes = sum(3 in k for k in counters)
    return twos * threes

def prob2(s):
    for a, b in combinations(s, 2):
        dist = _cmp(a, b)
        # dist = lv.distance(a, b)
        if dist == 1:
            out = "".join(c1 for c1, c2 in zip(a, b) if c1 == c2)
            return out


if __name__ == "__main__":
    inp = sys.stdin.read().splitlines()
    print(prob1(inp))
    print(prob2(inp))