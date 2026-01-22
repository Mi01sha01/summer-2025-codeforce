import sys 
input = sys.stdin.readline

t = int(input(). strip())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    b = True
    
    for i in range(n - 1):
        diff = abs(a[i] - a[i + 1])
        
        if diff != 5 and diff != 7:
            b = False
            break
        
    
    print("Yes" if b else "No")       
    
            