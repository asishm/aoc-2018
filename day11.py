from itertools import product
import numpy as np
import pandas as pd
from numba import jit

def gen_np(xsize, ysize, special_inp, debug=False):
    grid = pd.DataFrame(list(product(range(1,xsize+1), range(1,ysize+1))), columns=['x', 'y'])
    grid['power'] = (((grid.x + 10 )*grid.y + special_inp) * (grid.x + 10 ) // 100) % 10 - 5
    fin = grid.pivot_table(index='x', columns='y')
    if debug:
        print(fin)
    return fin.values
    
@jit(nopython=True)
def f(fin, kern_min, kern_max):
    x,y,g = 0,0,0
    maxv = fin[0][0]
    for kern in range(kern_min,kern_max):
        for i in range(fin.shape[0]):
            for j in range(fin.shape[1]):
                s = fin[i:i+kern, j:j+kern].sum()
                if s > maxv:
                    maxv = s
                    x = i+1
                    y = j+1
                    g = kern
    return maxv, x, y, g

if __name__ == "__main__":
    v1 = gen_np(300, 300, 2187)
    print(f(v1,3,4))
    print(f(v1, 1, 21))