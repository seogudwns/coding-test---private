# https://www.acmicpc.net/problem/1004

from sys import stdin

cases = int(stdin.readline())

for _ in range(cases):
    x1,y1,x2,y2 = map(int,stdin.readline().strip().split())
    
    result = 0
    for _ in range(int(stdin.readline())):
        x,y,half = map(int,stdin.readline().strip().split())
        half_sq = half**2
        stt_bd = (x-x1)**2 + (y-y1)**2
        end_bd = (x-x2)**2 + (y-y2)**2
        
        if max(stt_bd,end_bd)<half_sq or min(stt_bd,end_bd)>half_sq:
            continue
        result += 1
    
    print(result)
