t = int(input())
for _ in range(t):
    input()  
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = j = 0
    res = []
    lines = k
    possible = True

    while i < n or j < m:
        moved = False

        if i < n and a[i] == 0:
            res.append(0)
            lines += 1
            i += 1
            moved = True
        elif j < m and b[j] == 0:
            res.append(0)
            lines += 1
            j += 1
            moved = True
        elif i < n and a[i] <= lines:
            res.append(a[i])
            i += 1
            moved = True
        elif j < m and b[j] <= lines:
            res.append(b[j])
            j += 1
            moved = True

        if not moved:
            possible = False
            break

    if possible:
        print(' '.join(map(str, res)))
    else:
        print(-1)
