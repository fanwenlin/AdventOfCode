import sys
import numpy as np

lines = [line for line in sys.stdin]
numbers = [list(map(int, line.split())) for line in lines[:-1]]
operators = lines[-1].split()

cols = len(numbers[0])
rows = len(numbers)

s = numbers[0][:]
numbersT = np.transpose(numbers)
ans1 = 0
for i in range(cols):
    ans1 += np.sum(numbersT[i]) if operators[i] == '+' else np.prod(numbersT[i])

print('ans1: ',ans1)

operators_idx = []
for i in range(len(lines[-1])):
    if lines[-1][i] == ' ':
        continue
    else:
        operators_idx.append(i)
operators_idx.append(len(lines[-1]))
ops_ranges = list(zip(operators_idx[:-1], operators_idx[1:], operators))

linesT = np.transpose(np.array([list(line) for line in lines[:-1]], dtype=str))

ans2 = 0
for row_begin, row_end, op in ops_ranges:
    numbers = list(map(int, [''.join(line).strip() for line in linesT[row_begin:row_end].tolist() if ' '.join(line).strip() != '']))
    ans2 += np.sum(numbers) if op == '+' else np.prod(numbers)

print('ans2: ',ans2)
