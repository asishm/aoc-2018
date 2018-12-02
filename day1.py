from itertools import cycle
import sys

def prob1(s):
    return sum(s)

def prob2(s):
    seen = set([0])
    start = 0
    for val in cycle(s):
        start += val
        if start in seen:
            return start
        seen.add(start)

if __name__ == "__main__":
    inp = list(map(int, sys.stdin.read().splitlines()))
    print(prob1(inp))
    print(prob2(inp))