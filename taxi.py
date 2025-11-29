num_groups=int(input())
groups=list(map(int,input().split()))
taxi=0
c1=groups.count(1)
c2=groups.count(2)
c3=groups.count(3)
c4=groups.count(4)
taxi+=c4
taxi+=c3
c1=max(0,c1-c3)
taxi+=(c2//2)
if c2%2==1:
    taxi+=1
    c1=max(0,c1-2)
taxi+=(c1+3)//4
print(taxi)