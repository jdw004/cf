t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    xa = 0
    xb = 0
    lastDiff = -1

    for i in range(n):
        xa ^= a[i]
        xb ^= b[i]
        if a[i] != b[i]:
            lastDiff = i

    if xa == xb:
        print("Tie")
    else:
        if lastDiff % 2 == 0:
            print("Ajisai")
        else:
            print("Mai")
