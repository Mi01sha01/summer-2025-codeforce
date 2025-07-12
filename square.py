t = int(input())
for _ in range(t):
    x_coords = []
    y_coords = []
    for _ in range(4):
        x, y = map(int, input().split())
        x_coords.append(x)
        y_coords.append(y)

    side = max(max(x_coords) - min(x_coords), max(y_coords) - min(y_coords))
    print(side * side)
