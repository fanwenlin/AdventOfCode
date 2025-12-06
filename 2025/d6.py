# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  

import sys



lines = [line for line in sys.stdin]
numbers = [list(map(int, line.split())) for line in lines[:-1]]
operators = lines[-1].split()


cols = len(numbers[0])
# print(cols)
# print(numbers)
# print(operators)
rows = len(numbers)
# print(rows)

ans1 = 0

s = numbers[0][:]
for j in range(cols):
    for i in range(1,rows):
        if operators[j] == '*':
            s[j] *= numbers[i][j]
        elif operators[j] == '+':
            s[j] += numbers[i][j]
    ans1 += s[j]

print(ans1)

operators_idx = []
for i in range(len(lines[-1])):
    if lines[-1][i] == ' ':
        continue
    else:
        operators_idx.append(i)
operators_idx.append(len(lines[-1]))
# print(operators_idx)
# next_operator_idx = operators_idx[1:] + [cols]

s2numbers = [[]] * cols

for j in range(cols):
    s2numbers[j] = [''] * (operators_idx[j+1] - operators_idx[j])
    # print(j, operators_idx[j], operators_idx[j+1])
    for i in range(rows):
        for k in range(operators_idx[j], operators_idx[j+1]):
            s2numbers[j][k - operators_idx[j]] += lines[i][k]


s2 = [1 if o == '*' else 0 for o in operators]

for j in range(cols):
    
    # print(j, s2numbers[j], s2[j])
    # print('join:', operators[j].join([s.strip() for s in s2numbers[j] if s.strip() != '']))

    s2[j] = int(eval(operators[j].join([s.strip() for s in s2numbers[j] if s.strip() != ''])))

print(sum(s2))
