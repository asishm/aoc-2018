from numba import jit

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

@jit(nopython=True)
def solve2(n):
    p1, s1 = 0,3
    p2, s2 = 1,7
    scores = [3,7]
    score_len = 2
    while True:
        nexts = s1 + s2
        if nexts >= 10:
            to_add = divmod(nexts,10)
            scores.append(to_add[0])
            if scores[-len(n):] == n:
                return score_len + 1 - len(n)
            scores.append(to_add[1])
            score_len += 2
        else:
            scores.append(nexts)
            score_len += 1
        p1 = (p1 + s1 + 1) % score_len
        p2 = (p2 + s2 + 1) % score_len
        s1 = scores[p1]
        s2 = scores[p2]
        if scores[-len(n):] == n:
            return score_len - len(n)

if __name__ == "__main__":
    print("Part 1: ", solve(286051))
    print("Part 2: ", solve2([2,8,6,0,5,1]))