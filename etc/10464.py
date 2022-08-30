# https://www.acmicpc.net/problem/10464

'''
4n ~ 4n+3 까지 xor = 0
'''

from sys import stdin

def xor_calc(start,end):
    result = 0
    if end-start<=4:
        for i in range(start,end+1):
            result ^= i
        print(result)
        return
    
    stt_start = (start//4)*4
    for i in range(start,stt_start+4):
        result ^= i
        
    stt_end = (end//4)*4
    for i in range(stt_end,end+1):
        result ^= i
    
    print(result)
    return

cases = int(stdin.readline().strip())
for _ in range(cases):
    start,end = map(int,stdin.readline().strip().split())
    xor_calc(start,end)
