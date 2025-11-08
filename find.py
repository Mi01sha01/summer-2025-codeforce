t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    seen = {}
    ok = True

    for i in range(n):
        ch = s[i]
        parity = i % 2  # 0 for even, 1 for odd
        if ch in seen:
            if seen[ch] != parity:
                ok = False
                break
        else:
            seen[ch] = parity

    print("YES" if ok else "NO")