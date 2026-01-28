n, m = map(int, input().split())
a = n // m
b = n % m
fr = [a] * m

for i in range(b):
    fr[i] += 1
    
print(*fr)    
    