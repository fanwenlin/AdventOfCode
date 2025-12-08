import sys
import numpy as np

lines = [line for line in sys.stdin]
points = [list(map(int, line.split(','))) for line in lines]

def distance(p1, p2): return sum((a-b)**2 for a, b in zip(p1, p2))
distances = sorted([ (distance(p1, p2), i, j) for j, p2 in enumerate(points) for i, p1 in enumerate(points) if i < j], key=lambda x: x[0])

root, size = list(range(len(points))), [1] * len(points)

def find(x):
    if root[x] == x:
        return (x, size[x])
    (root[x], size[x]) = find(root[x])
    return (root[x], size[x])

def union(i, j) -> bool:
    (rooti, sizei) = find(i)
    (rootj, sizej) = find(j)
    if rooti == rootj:
        return False
    
    if sizei < sizej:
        root[rooti] = rootj
        size[rootj] += size[rooti]
    else:
        root[rootj] = rooti
        size[rooti] += size[rootj]
    return True

groups = []
last_connected = None

for idx, (_, i, j) in enumerate(distances):
    if idx+1 == 1000:
        groups = [(size[i], i) for i in range(len(points)) if root[i] == i]
    if union(i, j):
        last_connected = (i, j)
            
if not groups:
    groups = [(size[i], i) for i in range(len(points)) if root[i] == i]

if len(groups) > 3:
    groups = sorted(groups, key=lambda x: x[0], reverse=True)[:3]

print('ans1: ', np.prod([x[0] for x in groups]))
print('ans2: ', points[last_connected[0]][0]* points[last_connected[1]][0])
