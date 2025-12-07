import sys

lines = [line for line in sys.stdin]
start = [c == 'S' for c in lines[0]]
seperators = [[c == '^' for c in line] for line in lines[1:]]

s = start[:]
ans1 = 0
for seperator in seperators:
    seperated = [si if si and seperatori else 0 for si, seperatori in zip(s, seperator)]
    ans1 += len(seperated) - seperated.count(0)
    s = [sum(si) for si in zip(s, [0] + seperated[:-1], seperated[1:] + [0], [-si for si in seperated])]

print('ans1: ',ans1)
print('ans2: ', sum(s))    
    