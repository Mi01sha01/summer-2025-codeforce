n = int(input())
if n % 2 != 0:
    print(-1)
else:
    a = []    
    for i in range(1,n+1):
        if i % 2== 0:
            a.append(i)
            a.append(i-1)
            
    print(*a)
    
