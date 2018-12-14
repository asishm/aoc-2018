from tqdm import tqdm
from itertools import cycle

class Elf:
    def __init__(self, pos, score):
        self.pos = pos
        self.score = score

def solve(n):
    e1 = Elf(0, 3)
    e2 = Elf(1, 7)

    scores = [3, 7]

    while len(scores) < n + 10:
        nexts = e1.score + e2.score
        if nexts >= 10:
            to_add = [nexts // 10, nexts % 10]
            scores.extend(to_add)
        else:
            scores.append(nexts)
        e1.pos = (e1.pos + e1.score + 1) % len(scores)
        e2.pos = (e2.pos + e2.score + 1) % len(scores)
        e1.score = scores[e1.pos]
        e2.score = scores[e2.pos]
    return int(''.join(map(str, scores[n:n+10])))

def solve2(n):
    e1 = Elf(0, 3)
    e2 = Elf(1, 7)

    n = str(n)
    nlen = len(n)
    scores = [3, 7]

    while True:
        nexts = e1.score + e2.score
        if nexts >= 10:
            to_add = divmod(nexts, 10)
            scores.extend(to_add)
        else:
            scores.append(nexts)
        e1.pos = (e1.pos + e1.score + 1) % len(scores)
        e2.pos = (e2.pos + e2.score + 1) % len(scores)
        e1.score = scores[e1.pos]
        e2.score = scores[e2.pos]
        k = ''.join(map(str, scores[-nlen - 2:]))
        if n in k:
            return ''.join(map(str, scores)).index(n)

if __name__ == "__main__":
    print("Part 1: ", solve(286051))
    print("Part 2: ", solve2(286051))