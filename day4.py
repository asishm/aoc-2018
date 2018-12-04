from collections import defaultdict
import sys
# import pandas as pd
import re
from datetime import datetime
from pprint import pprint

def parse_line(s):

    return 

def prob1(s):
    # print("\n".join(s))
    prev = None
    prev_slept = None
    data = {}
    for line in s:
        if 'Guard' in line:
            _id = re.findall(r'\d+', line)[-1]
            prev = int(_id)
        elif 'asleep' in line:
            prev_slept = int(re.findall(r'\d+', line)[-1])
        elif 'wakes up' in line:
            slept = int(re.findall(r'\d+', line)[-1])
            if prev not in data:
                data[prev] = [slept - prev_slept + 1, [0] * 60]
            else:
                data[prev][0] += (slept - prev_slept + 1)
            for i in range(prev_slept, slept):
                data[prev][1][i] += 1
            # print(line, prev, slept, prev_slept)
            # print(data)
            # print(prev, prev_slept, duration, line)

    # print(data)
    _id, res = max(data.items(), key=lambda x: x[1][0])
    # print(_id)
    # print(res[0])
    # print(res[1])
    
    return _id * res[1].index(max(res[1])), data

def prob2(data):
    # print(data)
    vals = {k: (v[1].index(max(v[1])), max(v[1])) for k, v in data.items()}
    # print(vals)
    out = max(vals.items(), key=lambda x: x[1][1])

    return out[0] * out[1][0]

if __name__ == "__main__":
    inp = sorted(sys.stdin.read().splitlines())
    out, data = prob1(inp)
    print(out)
    print(prob2(data))