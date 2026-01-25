import sys
input = sys.stdin.readline
 
t = int(input().strip())
for _ in range(t):
          n = int(input())
          
          if n < 2:
              print(1)
          else:
               print(n // 2 if n % 2 == 0 else n // 2 + 1)