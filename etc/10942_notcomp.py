# https://www.acmicpc.net/problem/10942

# from sys import stdin

# N = int(stdin.readline())
# arr = list(map(int,stdin.readline().strip().split()))

# pal = [[0]*(N+1) for _ in range(N+1)]
# def check_pal(start,end):
#     if end == start:
#         return 1
#     mid = (end+1-start)//2
#     for i in range(mid):
#         if arr[start+i] != arr[end-i]:
#             return 0
        
#     return 1

# for i in range(1,N+1):
#     for j in range(i,N+1):
#         pal[i][j] = check_pal(i-1,j-1)
        
# for _ in range(int(stdin.readline())):
#     stt,end = map(int,stdin.readline().strip().split())
#     print(pal[stt][end])

# ! time over.

from sys import stdin

N = int(stdin.readline())
arr = list(map(int,stdin.readline().strip().split()))

pal = [[0]*(N+1) for _ in range(N+1)]
def check_pal(start,end):
    if end == start:
        return 1
    mid = (end+1-start)//2
    for i in range(mid):
        if arr[start+i] != arr[end-i]:
            return 0
        
    return 1

for i in range(1,N+1):
    for j in range(i,N+1):
        pal[i][j] = check_pal(i-1,j-1)    # --> 여기서 효율성을 끌어올려야함. 재사용을 할 필요성이 있음.
        
for _ in range(int(stdin.readline())):
    stt,end = map(int,stdin.readline().strip().split())
    print(pal[stt][end])