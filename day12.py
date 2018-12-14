import sys

def parse(inp):
    ini = inp[0].split(':')[1].strip()
    mapping = dict(tuple(k.split(' => ')) for k in inp[2:])

    return ini, mapping

def solve_org(ini, mapping, s=5, e=20, niter=20, debug=False):
    ini_state = list('.' *s + ini + '.'*e)
    state = ini_state[:]
    sums = []
    for _ in range(niter):
        n_state = ['.'] * len(state)
        for i in range(len(state)):
            p = state[max(i-2,0):i+3]
            if i < 2:
                p = ''.join(['.'] * (5 - len(p)) + p)
            if i > len(state) - 3:
                p = ''.join(p + ['.'] * (5 - len(p)))
            p = ''.join(p)
            n_state[i] = mapping.get(p, '.')
        sums.append(sum(idx for idx, char in enumerate(n_state, -s) if char == '#'))
        if debug:
            print(''.join(n_state))
        state = n_state
    return sums, ''.join(state)

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    ini, mapping = parse(data)

    sums, final_state = solve_org(ini, mapping, 1000, 1000, 200)
    print("Part 1: ", sums[19])

    diff = sums[-1] - sums[-2]
    print("Part 2: ", sums[-1] + diff * (50_000_000_000 - 200))