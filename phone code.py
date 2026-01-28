n = int(input())
nums = [input().strip() for i in range(n)]

ans = 0
for num in zip(*nums):
    if len(set(num)) == 1:
        ans += 1
    else:
        break
            
print(ans)

