ans = 0
cur = 50
while True:
    try:
        x = input()
        d = -1 if x[0] == 'L' else 1
        num = int(x[1:])
    except Exception as e:
        break
    before = cur
    # cur += num*d
    for i in range(num):
        cur += d
        if cur % 100== 0:
            ans = ans+1
            # print(cur)
    
    # if cur %100 == 0:
    #     ans = ans +1
    # elif (before//100) != (cur // 100):
    #     ans = ans+abs(before//100 - ans//100)
    #     print(f'debug {before} {x} {abs(before//100 - cur//100)}')


print(ans)