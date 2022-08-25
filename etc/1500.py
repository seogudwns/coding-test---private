from sys import stdin

k,n = map(int,stdin.readline().strip().split())

small,residue = divmod(k,n)

result = 1
for _ in range(n-residue):
    result = (result*small)

big = small + 1
for _ in range(residue):
    result = (result*big)

print(result%9223372036854775807) # init code.