import sys
input = sys.stdin.readline
 
t = int(input().strip())
for _ in range(t):
   a, b = map(int, input().split())
   
   if a == b:
             print(0)
   else:
       x = a - b
       if x > 0:
              print(1 if x % 2 == 0 else 2)
       else:
            print(1 if x % 2 != 0 else 2)