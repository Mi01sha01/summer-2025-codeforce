n = int(input())
club1 = []
club2 = []
for _ in range(n):
    names = input()
    
    if names in club1 or len(club1) == 0:
        club1.append(names)
    else:
        club2.append(names)
        
if len(club1) > len(club2):
    print(club1[0])
else:
    print(club2[0])   
         