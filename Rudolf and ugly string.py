t = int(input())
for _ in range(t):
        n = int(input())
        s = input()
        a = s.count("map")
        b = s.count("pie")
        c = s.count('mapie')
        print(a + b - c)
        
        