# https://www.acmicpc.net/problem/11478

from sys import stdin

arr = stdin.readline().strip()
leng = len(arr)
cnt = set()
for i in range(leng):
    for j in range(i+1,leng+1):
        cnt.add(arr[i:j])

print(len(cnt))