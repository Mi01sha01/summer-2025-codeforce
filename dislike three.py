t = int(input())
for i in range(t):
    k = int(input())
    count = 0
    num = 1
    while True:
        if num % 3 != 0 and num % 10 != 3:
            count += 1
            if count == k:
                print(num)
                break
        num += 1
