def solve():
    t = int(input())
    for _ in range(t):
        x = int(input())
        doors = list(map(int, input().split()))

        opened = [False] * 3
        key = x
        ok = True

        for _ in range(3):
            if key == 0 or opened[key - 1]:
                ok = False
                break
            opened[key - 1] = True
            key = doors[key - 1]

        print("YES" if ok else "NO")