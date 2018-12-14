import sys

def solve(inp, debug=False):
    part1 = None
    first = False
    track_cart_map = {
        "<": "-",
        ">": "-",
        "^": "|",
        "v": "|"
    }
    track_dir_map = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0)
    }
    grid = []
    carts = {}
    for i, row in enumerate(inp.splitlines()):
        tmp = []
        for j, val in enumerate(row):
            if val in "<>^v":
                tmp.append(track_cart_map[val])
                carts[(i, j)] = [track_dir_map[val], "left"]
            else:
                tmp.append(val)
        grid.append(tmp)
    
    def get_int_dir(cur_dir, to_turn):
        if cur_dir == (0, 1):
            return (-1, 0) if to_turn == 'left' else (1, 0)
        if cur_dir == (1, 0):
            return (0, 1) if to_turn == 'left' else (0, -1)
        if cur_dir == (0, -1):
            return (1, 0) if to_turn == 'left' else (-1, 0)
        if cur_dir == (-1, 0):
            return (0, -1) if to_turn == 'left' else (0, 1)
    
    def get_next_coord(grid, i, j, carts):
        cur_dir, next_int_dir = carts[(i, j)]

        next_x, next_y = (i + cur_dir[0], j + cur_dir[1])
        next_grid_val = grid[next_x][next_y]
        
        get_map = {
            (0, 1, '/'): (-1, 0),
            (0, -1, '/'): (1, 0),
            (1, 0, '/'): (0, -1),
            (-1, 0, '/'): (0, 1),
            (0, 1, '\\'): (1, 0),
            (0, -1, '\\'): (-1, 0),
            (1, 0, '\\'): (0, 1),
            (-1, 0, '\\'): (0, -1)
        }
        
        if next_grid_val == "/":
            return (next_x, next_y), [get_map[(cur_dir[0], cur_dir[1], next_grid_val)], next_int_dir]
        if next_grid_val == "\\":
            return (next_x, next_y), [get_map[(cur_dir[0], cur_dir[1], next_grid_val)], next_int_dir]
        
        if grid[next_x][next_y] == "+":
            if next_int_dir == 'left':
                return (next_x, next_y), [get_int_dir(cur_dir, next_int_dir), 'straight']
            elif next_int_dir == "straight":
                return (next_x, next_y), [cur_dir, 'right']
            else:
                return (next_x, next_y), [get_int_dir(cur_dir, next_int_dir), 'left']
        return (next_x, next_y), [cur_dir, next_int_dir]
        
    if debug:
        pass
#         print("\n".join(["".join(row) for row in grid]))

    def get_next_cart(carts):
        return sorted(carts.items(), key=lambda x: (x[0][0], x[0][1]))

    while True:
        if debug:
            print(carts)
        
        k2 = get_next_cart(carts)
        for (i, j), vals in k2:
            if (i, j) in carts:
                k, v = get_next_coord(grid, i, j, carts)

                del carts[(i, j)]
                if k in carts:
                    if not first:
                        first = True
                        part1 = k, v
                    del carts[k]
                else:
                    carts[k] = v
                if debug:
                    print(i, j, vals, k, v)
        if debug:
            print(carts)
            print("======")
        if len(carts) <= 1:
            return carts, part1

if __name__ == "__main__":
    data = sys.stdin.read()
    carts, part1 = solve(data)
    print("Part 1:", part1[0][::-1])
    print("Part 2:", list(carts.items())[0][0][::-1])