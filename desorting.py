t = int(input())
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))
    
    b = sorted(a)
    diff = []
    
    if a != b:
        print(0)
        
    else:
        for i in range(n - 1):
            c = a[i+1] - a[i]
            
            if c % 2 == 0:
                diff.append((c//2) + 1)
            
            else:
                diff.append((c + 1)//2)   
                 
        print(min(diff))        
        
           
    