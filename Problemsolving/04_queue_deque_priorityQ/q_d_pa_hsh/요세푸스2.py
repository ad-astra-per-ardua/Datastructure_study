from collections import deque

N, K = map(int, input().split())

list = deque(x for x in range(1, N + 1))
result = []

for i in range(N):
    list.rotate(-K + 1)
    result.append(list.popleft())


print(f"<{', '.join(map(str,result))}>")