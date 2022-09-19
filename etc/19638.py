# https://www.acmicpc.net/problem/19638

from sys import stdin
import heapq

N,H_centi,T = map(int,stdin.readline().strip().split())
giants = []
for _ in range(N):
    heapq.heappush(giants,-int(stdin.readline()))
    
if -giants[0]<H_centi:
    print('YES')
    print(0)
    exit(0)

for i in range(1,T+1):
    heapq.heappush(giants,-max(1,(-heapq.heappop(giants))//2))
    if -giants[0]<H_centi:
        print('YES')
        print(i)
        exit(0)

print('NO')
print(-giants[0])

# ! O(T * log(N))