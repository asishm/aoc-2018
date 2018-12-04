import sys
import re
from collections import defaultdict
# import pandas as pd

def parse(line):
    return [int(k) for k in re.findall(r'\d+', line)]

def prob1(lines):
    grid = {}
    for _id, left, top, width, height in lines:
        for i in range(left, left + width):
            for j in range(top, top + height):
                grid[(i, j)] = grid.get((i, j), 0) + 1
    return grid, sum(x >= 2 for x in grid.values())

def alternate_prob2(lines, grid):
    for _id, left, top, width, height in lines:
        valid = True
        for i in range(left, left + width):
            for j in range(top, top + height):
                if grid[(i, j)] > 1:
                    valid = False
                    break
            if not valid:
                break
        else:
            return(_id)
            

def prob2(lines):
    data = []
    for _id, left, top, width, height in lines:
        for i in range(left, left + width):
            for j in range(top, top + height):
                data.append([_id, i, j])
    df = pd.DataFrame(data, columns=['id', 'i', 'j'])
    
    vals = df.groupby(['i', 'j']).size().reset_index(name='grid_count')
    print(vals.grid_count.ge(2).sum())
    # print(df.shape[0])

    df2 = df.merge(vals, on=['i', 'j'], how='inner')

    group = df2.groupby('id').apply(lambda x: x.grid_count.eq(1).all())
    print(group[group].index[0])
    # return vals

def solve(lines):
    from time import time

    start = time()

    grid = defaultdict(int)
    for _id, left, top, width, height in lines:
        for i in range(left, left + width):
            for j in range(top, top + height):
                grid[(i, j)] = grid.get((i, j), 0) + 1

    print(sum(x >= 2 for x in grid.values()))
    p1 = time()
    print(p1 - start)
    
    for _id, left, top, width, height in lines:
        valid = True
        for i in range(left, left + width):
            for j in range(top, top + height):
                if grid[(i, j)] > 1:
                    valid = False
                    break
            if not valid:
                break
        else:
            print(_id)
            break
    print(time() - p1)

if __name__ == "__main__":
    inp = sys.stdin.read().splitlines()

    lines = [parse(line) for line in inp]
    grid, out = prob1(lines)
    print(out)
    print(alternate_prob2(lines, grid))