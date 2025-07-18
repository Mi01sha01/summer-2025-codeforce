n,k=map(int,input().split())
a=[I*5 for I in range(1,n+1)]
b=240-k
c=0
for j in a:
    if b-j>=0 and n-1>=0:
        b-=j
        n-=1
        c+=1
print(c)    
