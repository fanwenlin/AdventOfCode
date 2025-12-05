s = 0
s2 = 0
for r in input().split(','):
    if '-' not in r:
        # print(r)
        continue
    x = r.split('-')
    begin, end = int(x[0]), int(x[1])
    # print(f'b {begin}, {end}')
    for i in range(begin, end+1):
        
        stri = str(i)
        if len(stri) %2 == 0:
            mid = len(stri)//2
            l, r = stri[:mid], stri[mid:]
            if l == r:
                s += i
        
        l = len(stri)
        for lp in range(1,l):
            if l % lp == 0:
                if stri == stri[:lp] * (l // lp):
                    # print(i)
                    s2 += i
                    break
            # print(i)
print(s)
print(s2)
