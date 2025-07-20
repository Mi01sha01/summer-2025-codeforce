n=int(input())
av_rooms=0
for i in range(n):
    p,q=map(int,input().split())
    if (p+2)<=q:
        av_rooms+=1
print(av_rooms)
