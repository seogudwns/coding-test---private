# https://www.acmicpc.net/problem/11053

from sys import stdin

n = int(stdin.readline())
lst = list(map(int,stdin.readline().strip().split()))

leng = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if lst[i]>lst[j]:
            leng[i] = max(leng[i],leng[j]+1)

print(max(leng))

# ! idx를 이용한 더 좋은 풀이가 있을 가능성이 높다.