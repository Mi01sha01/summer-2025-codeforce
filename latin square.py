t = int(input())
for _ in range(t):
    a = input()
    b = input()
    c = input()
    d = set('ABC')
    
    if "?" in a:
        a = list(a)
        a.remove('?')
        a = set(a)
        print(str(d - a)[2])
        
    elif "?" in b:
        b = list(b)
        b.remove('?')
        b = set(b) 
        print(str(d - b)[2])   
        
    else:
        c = list(c)
        c.remove('?')
        c = set(c)    
        print(str(d - c)[2])
        
        