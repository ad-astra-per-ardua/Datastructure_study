n,m = map(int,input().split())

list_S = []
list_M = []
count = 0

for i in range(n):
    input_S = input()
    list_S.append(input_S)
    
for i in range(m):
    input_M = input()
    list_M.append(input_M)
    
#print(list_S, list_M)
    
for i in range(m):
    if list_M[i] in list_S:
        count += 1

print(count)
