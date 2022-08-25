# https://www.acmicpc.net/problem/1725

from sys import stdin

N = int(stdin.readline().strip())

histo = [int(stdin.readline().strip()) for _ in range(N)]
seg_tree_max = [None]*(3*N) # 요게 minima. 조금 더 줄이라면 줄이겠지만 굳이? 인 정도 차이.

def init_tree(idx,start,end):
    if start == end:
        seg_tree_max[idx] = histo[start]
        return seg_tree_max[idx]
    
    mid = (start+end)//2
    seg_tree_max[idx] = max(init_tree(2*idx,start,mid),init_tree(2*idx+1,mid+1,end))
    return seg_tree_max[idx]

init_tree(1,0,N-1)

for i in range(len(bin(N))-1):
    1
