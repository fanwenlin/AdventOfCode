s = 0
s2 = 0
r = input()

while r != '':
    # print(f'readline:{r}')
    maxs = 0 
    a = 0

    maxprefix = [None] * 13
    maxprefix[0] = ''
    prefixs = [[]]* 13
    prefixs[0] = ['']
    
    for digit in r:
        digit = int(digit)
        maxs = max(maxs, a*10 + digit)
        if digit > a:
            a = digit
        for i in range(12):
            if maxprefix[i] is not None:
                prefixs[i+1].append(maxprefix[i] + str(digit))
        for i in range(1, 13):
            if prefixs[i]:
                maxprefix[i] = max(prefixs[i])
                prefixs[i] = [maxprefix[i]]
            
    maxs2 = int(maxprefix[12])
                
    # print(maxs)
    s += maxs
    s2 += maxs2
    try:
        r = input()
    except Exception as e:
        break
        

print(s)
print(s2)
