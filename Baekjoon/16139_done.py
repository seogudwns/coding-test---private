# https://www.acmicpc.net/problem/16139

# ! pypy통과 but python not 통과1..

from sys import stdin

arr = stdin.readline().strip()
leng = len(arr)
check = [[0]*(26) for _ in range(leng+1)]

for i in range(leng):
    check[i+1][ord(arr[i])-97] = 1
    for j in range(26):
        check[i+1][j] += check[i][j]

for _ in range(int(stdin.readline().strip())):
    word,start,end = stdin.readline().strip().split()
    word = ord(word)-97
    print(check[int(end)+1][word] - check[int(start)][word])

# ! pypy통과 but python not 통과2..

from sys import stdin

arr = stdin.readline().strip()
leng = len(arr)
check = [None for _ in range(97)]+[[0]*(leng+1) for _ in range(26)]

for i in range(leng):
    check[ord(arr[i])][i+1] = 1
    for j in range(97,123):
        check[j][i+1] += check[j][i]

for _ in range(int(stdin.readline().strip())):
    word,start,end = stdin.readline().strip().split()
    print(check[ord(word)][int(end)+1] - check[ord(word)][int(start)])

# ! python 통과.

from sys import stdin

arr = stdin.readline().strip()
leng = len(arr)
check = [[0 for _ in range(26)] for _ in range(2)]

check[1][ord(arr[0])-97] += 1
for i in range(1,leng):
    check.append(check[-1][:])
    check[i+1][ord(arr[i])-97] += 1

for _ in range(int(stdin.readline().strip())):
    word,start,end = stdin.readline().strip().split()
    word = ord(word)-97
    print(check[int(end)+1][word] - check[int(start)][word])
