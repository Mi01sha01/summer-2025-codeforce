for _ in range(int(input())):
    c = {}
    for i in range(int(input())):
        a, b = map(int, input().split())
        
        if a <= 10:
            c[i + 1] = b
    
    max_key = max(c, key=c.get)
    print(max_key)      