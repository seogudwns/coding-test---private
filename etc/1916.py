# https://www.acmicpc.net/problem/1916

# from sys import stdin

# n = int(stdin.readline())
# m = int(stdin.readline())

# move = {i:[] for i in range(1,n+1)}
# charge = {i:[] for i in range(1,n+1)}

# for _ in range(m):
#     start,end,val = map(int,stdin.readline().strip().split())
#     move[start].append(end)
#     charge[start].append(val)

# start,end = map(int,stdin.readline().strip().split())

# check = [0 for _ in range(n+1)]
# check[start] = 1

# results = set()

# def dfs(start,val):
#     if start == end:
#         results.add(val)
#         return

#     for idx,i in enumerate(move[start]):
#         if check[i] == 0:
#             check[i] = 1
#             dfs(i,val+charge[start][idx])
#             check[i] = 0
            
#     return

# dfs(start,0)

# print(min(results))
# # print(results)

# ! init code.

# from sys import stdin
# from collections import deque

# n = int(stdin.readline())
# m = int(stdin.readline())
# maxi = 100000001
# move_charge = [[] for _ in range(n+1)]
# values = [maxi for _ in range(n+1)]

# for _ in range(m):
#     start,end,val = map(int,stdin.readline().strip().split())
#     move_charge[start].append((end,val))

# start,end = map(int,stdin.readline().strip().split())

# values[start] = 0
# Q = deque([start])
# while Q:
#     stt = Q.popleft()
#     val = values[stt]
#     for nex,move_v in move_charge[stt]:
#         if move_v>values[nex]:
#             continue
        
#         next_v = val+move_v
#         if values[nex] > next_v:
#             values[nex] = next_v
#             if nex != end:
#                 Q.append(nex)

# print(values[end])
# # print(values)

# ! 빨라졌지만 time over.

from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
maxi = 100000001
move_charge = [[] for _ in range(n+1)]
values = [maxi for _ in range(n+1)]

for _ in range(m):
    start,end,val = map(int,stdin.readline().strip().split())
    move_charge[start].append((val,end))

start,end = map(int,stdin.readline().strip().split())

values[start] = 0
Q = [(0,start)]
while Q:
    val,stt = heapq.heappop(Q)
    if val>values[stt]:
        continue
        
    for move_v,nex in move_charge[stt]:
        next_v = val+move_v
        if values[nex] > next_v:
            values[nex] = next_v
            heapq.heappush(Q,(next_v,nex))

print(values[end])
# print(values)