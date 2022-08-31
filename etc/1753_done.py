# https://www.acmicpc.net/problem/1753

# from sys import stdin
# from collections import deque

# maxi = 6000000000

# n,m = map(int,stdin.readline().strip().split())

# dist = [maxi for _ in range(n+1)]
# direc = [[] for _ in range(n+1)]
# start = int(stdin.readline())
# dist[start] = 0

# for _ in range(m):
#     stt,end,val = map(int,stdin.readline().strip().split())
#     direc[stt].append((end,val))

# Q = deque([(start,0)])
# while Q:
#     stt,val = Q.popleft()
#     if dist[stt]<val:
#         continue
    
#     for nex,move_v in direc[stt]:
#         next_v = move_v+val
#         if dist[nex]>next_v:
#             dist[nex] = next_v
#             Q.append((nex,next_v))

# for i in range(1,n+1):
#     print(dist[i] if dist[i] != maxi else 'INF')

# ! 중복이 있는지를 따지는 것이 있는데 이를 제낌..

# from sys import stdin
# from collections import deque

# maxi = 3000000

# n,m = map(int,stdin.readline().strip().split())

# dist = [maxi for _ in range(n+1)]
# charge = [[maxi]*(n+1) for _ in range(n+1)]
# start = int(stdin.readline())
# dist[start] = 0

# for _ in range(m):
#     stt,end,val = map(int,stdin.readline().strip().split())
#     charge[stt][end] = min(charge[stt][end],val)

# Q = deque([(start,0)])
# while Q:
#     stt,val = Q.popleft()
#     if dist[stt]<val:
#         continue
#     for nex,move_v in enumerate(charge[stt]):
#         if nex == 0:
#             continue
        
#         next_v = move_v+val
#         if dist[nex]>next_v:
#             dist[nex] = next_v
#             Q.append((nex,next_v))

# for i in range(1,n+1):
#     print(dist[i] if dist[i] != maxi else 'INF')

# ! charge를 만드는데 메모리 초과.

# from sys import stdin
# from collections import deque

# maxi = 3000000

# n,m = map(int,stdin.readline().strip().split())

# dist = [maxi for _ in range(n+1)]
# direc = [[] for _ in range(n+1)]
# charge = [[] for _ in range(n+1)]
# start = int(stdin.readline())
# dist[start] = 0

# for _ in range(m):
#     stt,end,val = map(int,stdin.readline().strip().split())
#     try:
#         idx = direc[stt].index(end)
#         charge[stt][idx] = min(charge[stt][idx],val)
#     except:
#         direc[stt].append(end)
#         charge[stt].append(val)
    
#     # ! 여기서 시간초과가 나는 것 같은데..

# Q = deque([(start,0)])
# while Q:
#     stt,val = Q.popleft()
#     if dist[stt]<val:
#         continue
#     for move_v,nex in enumerate(direc[stt]):
#         next_v = charge[stt][move_v]+val
#         if dist[nex]>next_v:
#             dist[nex] = next_v
#             Q.append((nex,next_v))

# # print(dist)
# for i in range(1,n+1):
#     print(dist[i] if dist[i] != maxi else 'INF')

# ! 이걸로 다시 써보자.

from sys import stdin
import heapq

maxi = 3000000

n,m = map(int,stdin.readline().strip().split())

dist = [maxi for _ in range(n+1)]
charge = [[]*(n+1) for _ in range(n+1)]
start = int(stdin.readline())
dist[start] = 0

for _ in range(m):
    stt,end,val = map(int,stdin.readline().strip().split())
    charge[stt].append((val,end))
    
Q = [(0,start)]
while Q:
    val,stt = heapq.heappop(Q)
    if dist[stt]<val:
        continue
    for move_v,nex in charge[stt]:
        next_v = move_v+val
        if dist[nex]>next_v:
            dist[nex] = next_v
            heapq.heappush(Q,(next_v,nex))

for i in range(1,n+1):
    print(dist[i] if dist[i] != maxi else 'INF')