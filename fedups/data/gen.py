import random as rnd
import sys

def distr(deg):
    l = [1000//deg for _ in range(deg)]
    l[-1] = 1000 - sum(l[0:-1])
    for i in range(deg-1):
        dt = rnd.randint(-l[i] + 1, min(1000-sum(l[0:i]) - (deg - i)-1, l[i+1]))
        l[i] += dt
        l[i+1] -= dt
    rnd.shuffle(l)
    return [i/1000 for i in l]

N = 300
M = rnd.randint(N-1, min(20*N, N*(N-1)//2))
edgs = [(i, rnd.randint(0, i-1)) for i in range(1, N)]
A = [[0]*N for _ in range(N)]
p = [[0]*N for _ in range(N)]
for t in edgs:
    assert t[0] != t[1]
    A[t[0]][t[1]] = 1
    A[t[1]][t[0]] = 1

for d in range(N-1, M):
    t = rnd.randint(0, N*(N-1)/2 - d)
    brk = False
    for i in range(N):
        for j in range(i+1, N):
            if A[i][j] == 0:
                if t == 0:
                    A[i][j] = 1
                    A[j][i] = 1
                    brk = True
                    if d%100 == 0:
                        sys.stderr.write(str(d)+ '\n')
                        sys.stderr.flush()
                    break
                t -= 1
        if brk:
            break
    if not brk:
        sys.stderr.write('fail')
        sys.stderr.flush()

sys.stderr.write(str(sum([sum(l) for l in A])) +' '+ str(M))
sys.stderr.flush()

for i in range(1, N):
    neigh = []
    for j in range(N):
        if A[i][j] == 1:
            neigh.append(j)
    dist = distr(len(neigh))
    for k, v in enumerate(neigh):
        p[i][v] = dist[k]

P = rnd.randint(1, N-1)
F = rnd.randint(1, N-1)
while F == P:
    F = rnd.randint(1, N-1)
print(N, M, 0, F, P)
for u in range(N):
    for v in range(u+1, N):
        if not A[u][v] == 0:
            print(u, v, rnd.randint(1, 100), p[u][v], p[v][u])

