# https://www.acmicpc.net/problem/1629

# ! init

from sys import stdin

A,B,C = map(int,stdin.readline().strip().split())

print((A**B)%C)
'''
test1
1000 1234 965

795

test2
38685 99162 1234

329
'''


# real.

from sys import stdin

A,B,C = map(int,stdin.readline().strip().split())
result = 1
mul = 1
while B>100:
    for _ in range(B-B//100*100):
        result = (result*A)%C
        
    B = B//100
    for _ in range(100):
        mul = (mul*A)%C
    
    A = mul
    mul = 1
for _ in range(B):
    result = (result*A)%C
    
print(result)
