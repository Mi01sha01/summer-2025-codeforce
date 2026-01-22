import sys
input = sys.stdin.readline
  
t = int(input())

for _ in range(t):
    expr = input().strip()
    a, b = expr.split('+')
    print(int(a) + int(b))  