t = int(input())

for _ in range(t):
    n = int(input())
    ray = list(map(int, input().split()))

    ans = []
    for v in ray:
        if v == -1:
            ans.append(0)
        else:
            ans.append(v)

    if ray[0] == -1 and ray[-1] != -1:
        ans[0] = ans[-1]

    elif ray[0] != -1 and ray[-1] == -1:
        ans[-1] = ans[0]

    x = abs(ans[-1] - ans[0])
    print(x)
    print(*ans)


