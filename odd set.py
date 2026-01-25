import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
      n = int(input().strip()) 
      lis = map(int, input().strip().split())
      even = 0
      for i in lis:
          if i % 2 == 0:
              even += 1
      print("YES" if even == n else "NO")        