# https://www.acmicpc.net/problem/14425

from sys import stdin

N,M = map(int,stdin.readline().strip().split())

S = set()
for _ in range(N):
    S.add(stdin.readline().strip())

result = 0
for _ in range(M):
    if stdin.readline().strip() in S:
        result += 1

print(result)