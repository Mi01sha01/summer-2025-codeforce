t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n >= 2:
        m = a[0] + a[1] - 1
        if n >= 3:
            for i in range(2,n):
                m+=a[i]-1
    else:
        m=a[0]
    print(m)    