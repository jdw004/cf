t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    aRay = list(map(int, input().split()))
    bRay = list(map(int, input().split()))

    for i in range(0, n):
        if i == 0:
            a = aRay[i]
            b = bRay[i]
        if aRay[i] == bRay[i]:
            continue
        elif i % 2 == 0:
            #ajisai's turn
            if a == aRay[i] and a != bRay[i]:
                aRay[i], bRay[i] = bRay[i], aRay[i]
                a ^= aRay[i]
        elif i % 2 == 1:
            #mai's turn
            if b == bRay[i] and aRay[i] != b:
                aRay[i], bRay[i] = bRay[i], aRay[i]
                b ^= bRay[i]
    
    aXor = aRay[0]
    bXor = bRay[0]
    for i in range(1, n):
        aXor ^= aRay[i]
        bXor ^= bRay[i]

    if aXor == bXor:
        ans.append("Tie")
    elif aXor > bXor:
        ans.append("Ajisai")
    else:
        ans.append("Mai")

for res in ans:
    print(res)