# https://www.acmicpc.net/problem/2559

from sys import stdin

N,K = map(int,stdin.readline().strip().split())
temp = [0]+list(map(int,stdin.readline().strip().split()))

for i in range(N):
    temp[i+1] += temp[i]

result = -float('inf')
for i in range(N-K+1):
    result = max(result,temp[i+K]-temp[i])
    # print(temp[i+K]-temp[i])

print(result)


