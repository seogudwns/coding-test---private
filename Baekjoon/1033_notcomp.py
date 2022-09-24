from sys import stdin

N = int(stdin.readline())

corr = {i:[] for i in range(N)}
up = [1 for _ in range(N)]
for _ in range(N-1):
    a,b,p,q = map(int,stdin.readline().strip().split())
    corr[a].append(b)
    corr[b].append(a)
    print(corr)
    for i in corr[a]:
        up[i] *= p
    for j in corr[b]:
        up[j] *= q

    print(up)
    
print('---------')
print(up)

