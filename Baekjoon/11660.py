# https://www.acmicpc.net/problem/11660

from sys import stdin

n,m = map(int,stdin.readline().strip().split())
lst = [[0]*(n+1)]+[[0]+list(map(int,stdin.readline().strip().split())) for _ in range(n)]

for i in range(1,n+1):
    for j in range(2,n+1):
        lst[i][j] += lst[i][j-1]
    if i != 0:
        lst[i] = [lst[i][j]+lst[i-1][j] for j in range(n+1)]

for _ in range(m):
    y1,x1,y2,x2 = map(int,stdin.readline().strip().split())

    print(lst[y2][x2]+lst[y1-1][x1-1]-lst[y2][x1-1]-lst[y1-1][x2])