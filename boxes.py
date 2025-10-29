t=int(input())
for I in range(t):
    n,k=map(int,input().split())
    boxes=list(map(int,input().split()))
    a=sorted(boxes)
    
    if k>=2:
        print("Yes")
    elif len(set(boxes)) ==1:
        print("yes")
    elif boxes== a:
        
        print('yes') 
    else:
        print("NO")    