import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
      n, m = map(int, input().strip().split())
      probs = input().strip() 
      levs = set(probs)
      b = 0   
      for i in levs:
          a = probs.count(i)
          if a > m:
              b += m
          else:
              b += a
      print(7 * m - b)            