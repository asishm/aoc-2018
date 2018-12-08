from itertools import chain, combinations, permutations, zip_longest, product
from functools import reduce
import sys
import re
from collections import defaultdict, Counter
import string
print('imports done')

def parse(line):
    pass

def prob1(df, lim=10000):
    xs = [k[0] for k in df]
    ys = [k[1] for k in df]
    left = min(xs)
    right = max(xs)
    top = min(ys)
    bot =  max(ys)

    def solve(l, r, t, b, debug=False):
        print(l,r,t,b)

        out = {}
        region = {}
        for i in range(l, r+1):
            for j in range(t, b+1):
                closest = float('inf')
                closest_point = []
                dis = 0
                for idx, (x, y) in enumerate(df):
                    dist = abs(x - i) + abs(y - j)
                    dis += dist
                    if dist < closest:
                        closest = dist
                        closest_point = [(x, y)]
                    elif dist == closest:
                        if debug:
                            pass
                            # print('found existing closest:', i, j, closest, x, y, closest_point)
                        closest_point.append((x, y))
                if debug:
                    pass
                    # print(i, j, closest, closest_point)
                if len(closest_point) == 1:
                    pt = closest_point[0]
                    if pt not in out:
                        out[pt] = 1
                    else:
                        out[pt] += 1
                region[(i, j)] = dis
        return out, region
            # print(i, j, closest_point)
    # print(dict(out))
    out1, r1 = solve(left, right, top, bot, True)
    out2, r2 = solve(left-10, right+10, top-10, bot+10)

    max_ = float('-inf')
    for k in set(out1.keys()).union(set(out2.keys())):
        # print(k, out1[k], out2[k])
        if out1[k] == out2[k]:
            # print(k, out1[k])
            max_ = max(max_, out1[k])

    c = 0
    for k in set(r1.keys()).intersection(set(r2.keys())):
        if r1[k] == r2[k]:
            if r1[k] < 10000:
                # print(k, r1[k])
                c += 1
    # print(r2[(2,5)], r1[(2,5)])
    return max_, c

def prob2(line):    
    pass

if __name__ == "__main__":
    inp = [tuple(map(int, line.split(','))) for line in sys.stdin.read().splitlines()]

    print(prob1(inp))