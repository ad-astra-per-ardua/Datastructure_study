n,m = map(int,input().split())

list_S = []
count = 0

for i in range(n):
    input_S = input()
    list_S.append(input_S)
    
for i in range(m):
    input_M = input()
    if input_M in list_S:
        count += 1

print(count)
    
