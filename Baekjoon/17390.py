# https://www.acmicpc.net/problem/17390

from sys import stdin

N,Q = map(int,stdin.readline().strip().split())
lst = [0] + sorted(map(int,stdin.readline().strip().split()))

for i in range(N):
    lst[i+1] += lst[i]
    
for _ in range(Q):
    a,b = map(int,stdin.readline().strip().split())
    print(lst[b]-lst[a-1])