t = int(input())
for _ in range(t):
    n = int(input())
    odd = 0
    even = 0 
    can = list(map(int, input().split()))
    
    for i in can:
        if i % 2 != 0:
            odd += i 
        else:
            even += i 
            
    if even > odd:
        print("YES")            
    else:
        print("NO")        
    

 