a, b=map(int,input().split())
c = int(input())
n = int(input())

if a * n + b <= c * n and c >= a:
    r = 1
else:
    r = 0

print(r)