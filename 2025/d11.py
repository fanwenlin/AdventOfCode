import sys

lines = [line.strip() for line in sys.stdin]
names = [line.split(':')[0] for line in lines]
tos = [line.split(':')[1].split(' ') for line in lines]

name2idx = {name: i for i, name in enumerate(names)}

n = len(names)
for tonames in tos:
    for toname in tonames:
        if toname not in name2idx:
            name2idx[toname] = n
            names.append(toname)
            tos.append([])
            n += 1

you, out, svr, fft, dac = name2idx['you'], name2idx['out'], name2idx['svr'], name2idx['fft'], name2idx['dac']

tos = [[name2idx[toname] for toname in tonames if toname in name2idx ] for tonames in tos]

from collections import deque

ans2 = 0
indegree = [0] * n
q = deque()
for i in range(n):
    for to in tos[i]:
        indegree[to] += 1

for i in range(n):
    if indegree[i] == 0:
        q.append(i)

state1 = [0]*n
state1[you] = 1

state2 = [(0,0,0,0)] * n
state2[svr] = (1,0,0,0) # (cnt, hasfftcnt, hasdacnt, havebothcnt)

while q:
    cur = q.popleft()
    s1, s2 = state1[cur], state2[cur]
    for to in tos[cur]:
        state1[to] += s1
        state2[to] = [sum(s) for s in zip(s2, state2[to])]
        if to == fft:
            state2[to][1] += s2[0]
            state2[to][3] += s2[2]
        if to == dac:
            state2[to][2] += s2[0]
            state2[to][3] += s2[1]
        indegree[to] -= 1
        if indegree[to] == 0:
            q.append(to)
print('ans1: ', state1[out])
print('ans2: ', state2[out][3])