import sys
input = sys.stdin.readline
 
mapping = {"U": "D", "D": "U", "L": "L", "R": "R"}
 
t = int(input())
for _ in range(t):
    n = int(input())
    fir_row = input().strip()
    sec_row = "".join(mapping[c] for c in fir_row)
    print(sec_row)