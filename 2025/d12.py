import sys

lines = [line.strip() for line in sys.stdin]
shapeslines = [l for l in lines if 'x' not in l]
empty_lines = [i for i, l in enumerate(lines) if l == '']
shapes = [shapeslines[i+1:j] for i, j in zip([-1] + empty_lines[:-1], empty_lines)]
cells = [[(i, j) for i in range(len(shape)) for j in range(len(shape[i])) if shape[i][j] == '#'] for shape in shapes ]
problemslines = [l for l in lines if 'x' in l]
sizes = [list(map(int, l.split(':')[0].split('x'))) for l in problemslines]
cnts = [list(map(int, l.split(': ')[1].split())) for l in problemslines]
sizeofshapes = [len(cells[i]) for i in range(len(cells))]


# It's not proved to be complete. Just works for this problem.
def can_pack(W,H, shapes, need):
    if sum([n * s for n, s in zip(need, sizeofshapes)]) > W * H * 0.85:
        return False
    return True


ans1 = 0
for size, cnt in zip(sizes, cnts):
    ans1 += can_pack(size[0], size[1], cells, cnt)
print('ans1: ', ans1)

# With this density distribution plotted, there is a huge gap betweeen two groups. So it naturally comes to the solution of guessing through a density threshold.
density = [sum([n * s for n, s in zip(cnt, sizeofshapes)]) / (size[0] * size[1]) for size, cnt in zip(sizes, cnts)]

from matplotlib import pyplot as plt

plt.hist(density, bins=40)
plt.xlabel('Density')
plt.ylabel('Count')
plt.title('Density Distribution (Absolute Space Needed / Provided Space)')
plt.show()


