def solve():
    t = int(input())
    for _ in range(t):
        keyboard = input().strip()
        s = input().strip()

        # map each letter to its position
        pos = {}
        for i in range(26):
            pos[keyboard[i]] = i

        time = 0
        for i in range(1, len(s)):
            time += abs(pos[s[i]] - pos[s[i - 1]])

        print(time)