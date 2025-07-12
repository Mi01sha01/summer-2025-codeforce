t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    total = prefix[n]
    max_sum = 0

    for x in range(k + 1):  
        if 2 * x > n or (k - x) > (n - 2 * x):
            continue
        removed = prefix[2 * x] + (prefix[n] - prefix[n - (k - x)])
        max_sum = max(max_sum, total - removed)

    print(max_sum)
