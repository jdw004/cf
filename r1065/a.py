x = int(input())

for _ in range(x):
    n = int(input())
    cow, chicken = 0, 0
    count = 0

    for cow in range(n):
        for chicken in range(n):
            if 4 * cow + 2 * chicken == n:
                count += 1
    print(count)
