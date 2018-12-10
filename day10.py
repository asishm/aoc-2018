from numba import jit
import numpy as np
import re
import sys

@jit
def solve(values, x):
    marea = np.inf
    idx = 0
    for t in x:
        x = values[:,0] + values[:,2] * t
        y = values[:,1] + values[:,3] * t
        area = (x.max() - x.min()) * (y.max() - y.min())
        if area < marea:
            marea = area
            idx = t
    return [idx, marea]

def get_at_time_t(values, t):
    x = values[:,0] + values[:,2] * t
    y = values[:,1] + values[:,3] * t
    x = (x - x.min()).astype(np.uint16)
    y = (y - y.min()).astype(np.uint16)

    xrng = x.max()
    yrng = y.max()
    grid = [[' ']*(xrng +1) for _ in range(yrng + 1)]
    for a, b in zip(x, y):
        grid[b][a] = "#"
    return '\n'.join(''.join(row) for row in grid)


if __name__ == "__main__":
    data = [list(map(int, re.findall(r'-?\d+', line))) for line in sys.stdin.read().splitlines()]
    solved = solve(np.array(data), np.arange(20000))
    to_print = get_at_time_t(np.array(data), solved[0])
    # print("Part 2: ", solved[1])