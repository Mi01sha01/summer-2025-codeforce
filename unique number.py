def smallest_uniqeu_numbers():
    
    t = int(input())
    for _ in range(t):
        x = int(input())
        
        if x > 45:
            print(-1)
        else:
            numbers = []
            for i in range(9, 0, -1):
                if x >= i:
                    numbers.append(i)
                    x -= i 
                    
            n = sorted(numbers)  
            print(int("". join(map(str,n))))      
                  
smallest_uniqeu_numbers()