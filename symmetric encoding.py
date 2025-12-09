def encode(b):
  r = sorted(set(b))
  c = r.copy()
  c.reverse()
  maping = {}
  for i in range(len(r)):
         maping[c[i]] = r[i]
          
  s = ""
  for char in b: 
     s += maping[char]
                    
  return s
          
          
          
for _ in range(int(input())):
          n = int(input())
          b = input()
          print(encode(b))