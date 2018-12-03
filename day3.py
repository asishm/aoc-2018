import sys
import re
from collections import defaultdict
import pandas as pd

def parse(line):
    return (int(k) for k in re.findall(r'\d+', line))

def prob1(s):
    lines = [parse(line) for line in s]

    grid = {}
    for _id, left, top, width, height in lines:
        for i in range(left, left + width):
            for j in range(top, top + height):
                grid[(i, j)] = grid.get((i, j), 0) + 1
    return sum(x >= 2 for x in grid.values())

def prob2(s):
    lines = (parse(line) for line in s)

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

                

if __name__ == "__main__":
    inp = sys.stdin.read().splitlines()
    # print(prob1(inp))
    print(prob2(inp))