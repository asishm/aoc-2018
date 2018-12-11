from itertools import product
import numpy as np
# import pandas as pd
from numba import jit

# def gen_np(xsize, ysize, special_inp, debug=False):
#     grid = pd.DataFrame(list(product(range(1,xsize+1), range(1,ysize+1))), columns=['x', 'y'])
#     grid['power'] = (((grid.x + 10 )*grid.y + special_inp) * (grid.x + 10 ) // 100) % 10 - 5
#     fin = grid.pivot_table(index='x', columns='y').cumsum(axis=1).cumsum()
#     return fin.values

def power(x, y):
    rack = x + 10
    power = rack * y
    power += 2187
    power *= rack
    toret = (power // 100 % 10) - 5
    toret[0] = 0
    toret[:,0] = 0
    return toret.cumsum(axis=0).cumsum(axis=1)
    
@jit(nopython=True)
def solve(fin, min_kern, max_kern):
    x,y,g = 0,0,0
    maxv = fin[0][0]
    n = len(fin)
    for kern in range(min_kern,max_kern):
        for i in range(n - kern):
            for j in range(n - kern):
                s = fin[i][j] + fin[i+kern][j+kern] - fin[i][j+kern] - fin[i+kern][j]
                if s > maxv:
                    maxv = s
                    x = i
                    y = j
                    g = kern
    return maxv, x+1, y+1, g

if __name__ == "__main__":
    v1 = np.fromfunction(power, (301, 301))
    print(solve(v1, 3, 4))
    print(solve(v1, 1, 301))