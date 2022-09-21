from sys import stdin

N,M = map(int,stdin.readline().strip().split())

listen = set()
two = set()

for _ in range(N):
    listen.add(stdin.readline().strip())

for _ in range(M):
    arr = stdin.readline().strip()
    if arr in listen:
        two.add(arr)

print(len(two))
print(*sorted(two),sep='\n')