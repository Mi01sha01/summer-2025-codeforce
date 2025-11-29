g = list(map(int, input().split()))
gcl = sorted(g)
if gcl[2] - gcl[0] >= 10:
    print("check again")
else:
    print("final", gcl[1])    