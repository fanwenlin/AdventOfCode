import sys
import numpy as np

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

lines = [line for line in sys.stdin]
points = [list(map(int, line.split(','))) for line in lines]

def area(p1, p2): return (max(p1[0], p2[0]) - min(p1[0], p2[0])+1) * (max(p1[1], p2[1]) - min(p1[1], p2[1])+1)
areas = [area(p1, p2) for p1 in points for p2 in points if p1 != p2]

ans1 = max(areas)
print('ans1: ', ans1)

area2s = []
rbc = (94927, 50365)
rtc = (94927, 48406)

lowerthan = min([p1[1] for (p1, p2) in zip(points, points[1:])if p1[0] > rbc[0] and p2[0] <= rbc[0]])
upperthan = max([p1[1] for (p1, p2) in zip(points, points[1:])if p1[0] <= rtc[0] and p2[0] > rtc[0]])


for p in points:
    # upper points
    if p[1] >= 50365 and p[1] <= lowerthan:
        ncornor = (rbc[0], p[1])
        
        area2s.append((area(p, rbc), p, rbc))
    
    # lower points
    if p[1] <= 48406 and p[1] >= upperthan:
        ncornor = (rtc[0], p[1])
        area2s.append((area(p, rtc), p, rtc))

area2s = sorted(area2s, key=lambda x: x[0], reverse=True)

area2s = area2s[1:] # observed the first one is invalid

print('ans2: ', area2s[:10])

import matplotlib.pyplot as plt

for p1, p2 in zip(points[:-1], points[1:]):
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-')

_, p1, p2 = max(area2s)
plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'b-')
rt = (p2[0], p1[1])
lb = (p1[0], p2[1])
plt.plot([rt[0], p1[0]], [rt[1], p1[1]], 'g-')
plt.plot([rt[0], p2[0]], [rt[1], p2[1]], 'g-')
plt.plot([lb[0], p1[0]], [lb[1], p1[1]], 'g-')
plt.plot([lb[0], p2[0]], [lb[1], p2[1]], 'g-')

plt.show()