t=int(input())
for I in range (t):
    k=int(input())
    print(k-1)
    '''
    why x=k-1?
    x!+(x-1)!=(k-1)!+(k-2)!
             =(k-1).(k-2)!+(k-2)!
             =(k-2)!.k
             look at the k as a factor 
             in the expression.
    '''         
    