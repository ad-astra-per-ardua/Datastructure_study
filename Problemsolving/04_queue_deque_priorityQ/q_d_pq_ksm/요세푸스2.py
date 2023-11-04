import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1
# For graph traversal DFS,BFS Etc... set direction
dx = [1,0,-1,0]
dy = [0,1,0,-1]

MOD = 1_000_000_007
# setrecursionlimit(10**5)
input = lambda: stdin.readline().strip()

######### main code goes here #########
from collections import deque

n, k = map(int,input().split()) 
seat = deque(x for x in range(n, 0, -1))
lists = []

while len(seat) > 0:
    seat.rotate(k)
    temp = seat.popleft()
    lists.append(temp)

print(f"<{', '.join(map(str,lists))}>")
