def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ops = 0
        i = 0

        while i < n:
            j = i
            while j < n and (a[j] % 2) == (a[i] % 2):
                j += 1
            block_len = j - i
            ops += block_len - 1
            i = j

        print(ops)