from itertools import chain, combinations, permutations, zip_longest
from functools import reduce
import sys
import re
from collections import defaultdict, Counter
import string

def prob1(line):
    # print(len(line))
    while True:
        line2 = str(line)
        to_sub1 = "|".join(f"{l}{l.upper()}" for l in string.ascii_lowercase)
        to_sub2 = "|".join(f"{l.upper()}{l}" for l in string.ascii_lowercase)
        # pat = f'{to_sub1}|{to_sub2}'
        # print(to_sub1)
        line2 = re.sub(to_sub1, "", line2)
        line2 = re.sub(to_sub2, "", line2)
        if len(line2) == len(line):
            break
        else:
            line = line2
        # print(len(line), len(line2))
    return len(line)

def prob2(line):
    min_c = float('inf')
    for l in string.ascii_lowercase:
        line2 = line
        line2 = re.sub(l, '', line2, flags=re.I)      
        out = prob1(line2)
        # print(l, out)
        min_c = min(min_c, out)
    return min_c

if __name__ == "__main__":
    inp = sys.stdin.read().strip()

    print(prob1(inp))
    # print(prob2(inp))