t = int(input())
out = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    totalXor = 0
    for x in a: totalXor ^= x
    for x in b: totalXor ^= x

    if totalXor == 0:
        out.append("Tie")
        continue

    mostSignifigantBit = 1 << (totalXor.bit_length() - 1)
    
    for i in range(n - 1, -1, -1):
        if (a[i] ^ b[i]) & mostSignifigantBit:
            if i % 2 == 0:
                out.append("Ajisai")
            else:
                out.append("Mai")
            break

print('\n'.join(out))