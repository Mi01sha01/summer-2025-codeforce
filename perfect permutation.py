n = int(input())
if n % 2 != 0:
    print(-1)
else:
    a = []    
    for i in range(1, n+1, 2):
      a.append(i+1)
      a.append(i)
            
    print(*a)
    
    
            