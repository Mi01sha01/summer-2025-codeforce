# Trippi Troppi Solution 
import sys
input = sys.stdin.readline

t = int(input().strip())  

for _ in range(t):
    words = input().split()  
    modern_name = ''.join(word[0] for word in words)  
    print(modern_name)    