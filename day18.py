import sys
from collections import Counter, OrderedDict
import itertools

def get_neighbors(i, j, grid):
    s = (k for k in itertools.product(range(i-1, i+2), range(j-1, j+2)) if k != (i, j))
    return [k for k in s if 0 <=k[0]<len(grid) and 0 <= k[1] < len(grid[0])]

def next_iter(grid):
    k = [[' '] * len(grid[0]) for _ in range(len(grid))]

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == '.':
                tc = 0
                for m,n in get_neighbors(i, j, grid):
                    if grid[m][n] == '|':
                        tc += 1
                if tc >= 3:
                    k[i][j] = '|'
                else:
                    k[i][j] = '.'
            elif val == '|':
                tc = 0
                for m,n in get_neighbors(i, j, grid):
                    if grid[m][n] == '#':
                        tc += 1
                if tc >= 3:
                    k[i][j] = '#'
                else:
                    k[i][j] = '|'
            else:
                tc = 0
                lc = 0
                for m,n in get_neighbors(i, j, grid):
                    if grid[m][n] == '#':
                        lc += 1
                    elif grid[m][n] == '|':
                        tc += 1
                    if tc and lc:
                        k[i][j] = '#'
                    else:
                        k[i][j] = '.'
    return k

def solve(grid):
    for _ in range(10):
        grid = next_iter(grid)
    c = Counter([val for row in grid for val in row])
    return c['|'] * c['#']

def grid2str(grid):
    return '\n'.join([''.join(row) for row in grid])

def solve2(grid, n=1000000000):
    seen = OrderedDict()
    seen[grid2str(grid)] = 0
    i = 0
    while True:
        grid = next_iter(grid)
        i += 1
        grid_str = grid2str(grid)
        # print("After Iteration: ", i)
        print(grid_str)
        if grid_str in seen:
            break
        else:
            seen[grid_str] = i
    cycle_len = i - seen[grid_str]
    cycle_val = (n - seen[grid_str]) % cycle_len

    g = [k for k,v in seen.items() if v == cycle_val + seen[grid_str]][0]
    return g.count('|') * g.count("#")


if __name__ == "__main__":
    grid = sys.stdin.read().splitlines()
    print(solve(grid))
    print(solve2(grid))