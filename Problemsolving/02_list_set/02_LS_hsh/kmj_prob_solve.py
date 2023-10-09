N, M = map(int, input().split())

count = 0
c = set()
for _ in range(N):
        c.add(input().rstrip())
for _ in range(M):
    check = set(input().rsplit())
    if check & c:
        count += 1

print(count)