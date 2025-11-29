for _ in range(int(input())):
    n, m = map(int, input().split())
    x = input()
    s = input()
    a = 0
    for i in range(6):
        if s in x:
            print(a)
            break 
        else:
            x = 2*x
            a +=1
    if a == 6 and s not in x:
        print(-1)           