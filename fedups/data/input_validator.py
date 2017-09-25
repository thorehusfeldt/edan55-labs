#!/usr/bin/python

import re
import sys

fiveIntsRE = re.compile('^[1-9][0-9]* [1-9][0-9]* [0-9]+ [0-9]+ [0-9]+\n$')
roadRE = re.compile('^[0-9]+ [0-9]+ [1-9][0-9]* (1.0|1|0|0.[0-9]*) (1.0|1|0|0.[0-9]*)\n$')

line = sys.stdin.readline()
assert fiveIntsRE.match(line)
N, M, H, F, P = map(int, line.split())
assert 3 <= N <= 300
assert N/2 <= M <= N*(N-1)/2
assert 0 <= H < N
assert 0 <= F < N and F != H
assert 0 <= P < N and P != H and P != F


roads = [sys.stdin.readline() for _ in range(M)]
assert sys.stdin.readline() == ''

pout = [0.0]*N
for r in roads:
    if not roadRE.match(r):
        print(r)
    assert roadRE.match(r)
    u, v, t, p1, p2 = map(float, r.split())
    u = int(u)
    v = int(v)
    t = int(t)
    assert 0 <= u < N and 0 <= v < N
    assert 0 < t < 1000 #sync with probelm stmt
    assert 0 <= p1 <= 1 and 0 <= p2 <= 1
    pout[u] += p1
    pout[v] += p2
for i in range(N):
    if i == H:
        assert pout[i] == 0
    else:
        assert abs(pout[i] - 1.0) < 0.00001 # maybe pout should sum to 1000 or something.
print('ok')
sys.exit(42)
