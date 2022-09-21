# https://www.acmicpc.net/problem/9663
# ! 원하는 방향의 문제가 아니라 백준에 제출하지 않은 문제입니다. 다만 분석을 위해 컴으로 돌려보긴 함.

import time
n = int(input())

stt = time.time()
ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)
        
n_queens(0)

end = time.time()
print('sol : {}, before_time : {}'.format(ans,end-stt))

# ! 개선 코드. n == 12 기준으로 약 18% 정도의 시간을 절약하고, n이 클수록 절약되는 시간의 %가 커진다. 
# n = int(input())

stt = time.time()
ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(row[x-1]-1):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)
        
        for i in range(row[x-1]+1,n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)
                
for i in range(n//2):
    row[0] = i
    n_queens(1)
ans *= 2

if n%2: #odd case.
    row[0] = n//2
    n_queens(1)

end = time.time()
print('sol : {}, update_time : {}'.format(ans,end-stt))

'''
개선이 속도를 빠르게 하기는 하지만 여전히 느림., 
이걸 그대로 돌릴 경우 속도에 어느정도 편차가 있을 수는 있는데 메모리 리프레싱으로 인한 이슈라고 추측된다.
10 기준.
기존 속도 : 1.8493387699127197,
개선했을 때 속도 : 0.8064863681793213
11 기준.
기존 속도 : 10.00817322731018,
개선했을 때 속도 : 4.8483335971832275
12 기준.
기존 속도 : 58.5093252658844,
개선했을 때 속도 : 25.326098918914795
'''