import sys

def solve(inp, start=0):
    nnodes = inp[start]
    nmeta = inp[start+1]
    start += 2
    part1 = 0
    part2 = []

    for _ in range(nnodes):
        start, p1, p2 = solve(inp, start)
        part2.append(p2)
        part1 += p1
    if not part2:
        toret = sum(inp[start:start+nmeta])
        start += nmeta
        return start, part1 + toret, toret
    else:
        part2 = [0] + part2
        s = 0
        for val in inp[start: start+nmeta]:
            part1 += val
            try:
                s += part2[val]
            except IndexError:
                pass
        start += nmeta
        return start, part1, s

if __name__ == "__main__":
    inp = list(map(int,sys.stdin.read().split()))

    print(solve(inp)[1:])