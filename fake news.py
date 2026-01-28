s = input().strip()
target = "heidi"

j = 0
for c in s:
    if c == target[j]:
        j += 1
        if j == len(target):
            print("YES")
            break
else:
    print("NO")