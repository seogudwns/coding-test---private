# https://www.acmicpc.net/problem/2448

'''
xxx = '                       *                        '
print(len(xxx)) 
print(xxx.index('*'))
# 24를 넣었을 때 leng = 48
# 별의 위치 = 23


yyy = '                    *     *                     '
print(yyy.index('*'))  # 위치 : 20, 26

'''

# from collections import deque
# n = int(input())
# m = 0
# while 3*2**m != n:
#     m += 1

# start = ['  *  ',' * * ','*****']
# leng = 3
# for i in range(m):
#     x = start[i]
#     leng_null = n-1-len(x)
#     print(' '*leng_null+x+' '*(leng_null+1))
#     start.append(x+' '+x)

# ! 다른 방법으로 turn..

from collections import deque
from re import X
n = int(input())
m = 0
while 3*2**m != n:
    m += 1
print(m)
start = ['  *  ',' * * ','*****']

for i in start:
    print(i)

if m == 0:
    exit(0)

Q = deque(start)
Q_before = deque()
Q_after = deque()        

for _ in range(m):
    while Q:
        x = Q.popleft()
        print(x)
        Q_before.append(x)
        Q_after.append(x+' '+x)



'''
                       *
                      * *
                     *****
                       *                        
                      * *                       
                     *****                      
'''