import sys

ranges, endpoints = [], []

lines = [line.strip() for line in sys.stdin]
seperator_i = lines.index('')
ranges = [tuple(map(int, line.split('-'))) for line in lines[:seperator_i]]
endpoints = [item for sublist in ranges for item in sublist]
checkpoints = map(int, lines[seperator_i+1:])

ans1 = sum([any([xi <= x <= yi for xi, yi in ranges]) for x in checkpoints])

print(f'ans1: {ans1}')

endpoints = sorted(list(set(endpoints)))
ans2 = sum([(r - l - 1) for l,r in zip(endpoints[:-1], endpoints[1:]) if any([xi <= (l+1) <= yi for xi, yi in ranges])]) + len(endpoints)
print(f'ans2: {ans2}')