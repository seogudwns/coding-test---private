# https://www.acmicpc.net/problem/10830

from sys import stdin

n,m = map(int,stdin.readline().strip().split())
mat = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]
result = [[0]*n for _ in range(n)]
for i in range(n):
    result[i][i] = 1

def mat_mult(mat1,mat2,n):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += mat1[i][k]*mat2[k][j]
            result[i][j] = tmp%1000
    
    return result

while m != 0:
    if m%2 == 1:
        result = mat_mult(mat,result,n)
    
    m = m//2
    mat = mat_mult(mat,mat,n)
    
for i in result:
    print(*i)
