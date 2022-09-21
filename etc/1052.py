# https://www.acmicpc.net/problem/1052

from sys import stdin

N,K = map(int,stdin.readline().strip().split())

cnt = N
while bin(cnt).count('1')>K:
    cnt+=cnt&-cnt
    
print(cnt-N)

# ! 아래는 이걸로도 통과가 되는구나 싶어서 내비둔 코드.

# cnt = 0

# while bin(N).count('1') > K:
#     N += 1
#     cnt += 1

# print(cnt)