# https://www.acmicpc.net/problem/12844

# from sys import stdin

# end = int(stdin.readline().strip())
# start = 0
# lst = list(map(int,stdin.readline().strip().split()))

# cases = int(stdin.readline().strip())

# seg_tree = [None]*(4*end)
# end -= 1

# def make_seg_tree(idx,start,end):
#     # print('make_idx,start,end :',idx,start,end)
#     if start == end:
#         seg_tree[idx] = lst[start]
#         return seg_tree[idx]
    
#     mid = (start+end)//2
#     seg_tree[idx] = make_seg_tree(2*idx,start,mid) ^ make_seg_tree(2*idx+1,mid+1,end)
#     return seg_tree[idx]

# def update_seg_tree(idx,start,end,update_start,update_end,num):
#     if update_end<start or end<update_start:
#         return
#     elif (end-start)%2 == 0:
#         # print('change =',idx,start,end,seg_tree[idx],'to',seg_tree[idx]^num) 잘 된거 같다..?
#         seg_tree[idx] ^= num
#         if start == end:
#             return

#     mid = (start+end)//2
#     update_seg_tree(2*idx,start,mid,update_start,update_end,num)
#     update_seg_tree(2*idx+1,mid+1,end,update_start,update_end,num)
#     return

# '''
# 0 ~ 8 중
# 3 ~ 5 가정..
# 0 ~ 4.
# '''


# def xor_calc(idx,start,end,calc_start,calc_end):
#     # print('xor_calc input :',idx,start,end,calc_start,calc_end)
#     global result
#     if calc_start>end or calc_end<start:
#         return
    
#     mid = (start+end)//2
#     if calc_start<=start and end<=calc_end:
#         result ^= seg_tree[idx]
#         # print('calc_result :',seg_tree[idx])
#         return
    
#     xor_calc(2*idx,start,mid,calc_start,calc_end)
#     xor_calc(2*idx+1,mid+1,end,calc_start,calc_end)
#     return

# make_seg_tree(1,start,end)
# # print(seg_tree)

# for _ in range(cases):
#     order = tuple(map(int,stdin.readline().strip().split()))
#     # print(order)
#     if order[0] == 2:
#         result = 0
#         xor_calc(1,start,end,order[1],order[2])
#         print(result)
#     else:
#         update_seg_tree(1,start,end,order[1],order[2],order[3])
#         # print(seg_tree)

from sys import stdin

end = int(stdin.readline().strip())
start = 0
lst = list(map(int,stdin.readline().strip().split()))

cases = int(stdin.readline().strip())

seg_tree = [None]*(4*end)
lazy = [0]*(4*end)   
# --> 요걸 이용해야함..  2번 명령에서 바뀌는 부분은 바뀌고 이후에 바뀌어도 될 것은 lazy에 저장(start,end와 관계없이 저장, 
# 적용은 1번에서 쓸 때.), 필요시 바꾸는 연산을 진행해야함. 
# 1번 명령에서도 lazy가 있을 시 필요한 부분만 적용시키고 다시 나머지는 lazy에 저장.
end -= 1

def make_seg_tree(idx,start,end):
    if start == end:
        seg_tree[idx] = lst[start]
        return seg_tree[idx]
    
    mid = (start+end)//2
    seg_tree[idx] = make_seg_tree(2*idx,start,mid) ^ make_seg_tree(2*idx+1,mid+1,end)
    return seg_tree[idx]

def update_seg_tree(idx,start,end,update_start,update_end,num):
    # print('update_check :',idx,start,end,update_start,update_end) # done.
    # print(min(update_end,end),max(update_start,start))  # update 범위가 애매하게 겹칠 때를 고려할 필요가 있음.
    if update_end<start or end<update_start:  # 바뀌는 범위에 완전히 벗어나는 케이스.
        return
    elif (min(update_end,end)-max(update_start,start))%2 == 0: # xor이기 때문에 짝수번 연산이 되는 것은 없는 것과 동일. start == end일 경우 가장 기본 원소가 들어가고, 홀수의 경우(ex start : 2, end : 4 인 경우 2,3,4로 홀수 갯수.) (end-start)%2 == 0 이 성립.
        # print('update_change :',idx,start,end)  
        seg_tree[idx] ^= num
        if start == end:
            return

    mid = (start+end)//2
    update_seg_tree(2*idx,start,mid,update_start,update_end,num)
    update_seg_tree(2*idx+1,mid+1,end,update_start,update_end,num)
    return

def xor_calc(idx,start,end,calc_start,calc_end):
    # print('xor_calc input :',idx,start,end,calc_start,calc_end)
    if calc_start>end or calc_end<start:
        return 0
    
    mid = (start+end)//2
    if calc_start<=start and end<=calc_end:
        # print('calc :',seg_tree[idx],'& start,end : ',start,end)
        return seg_tree[idx]
    
    return xor_calc(2*idx,start,mid,calc_start,calc_end)^xor_calc(2*idx+1,mid+1,end,calc_start,calc_end)

make_seg_tree(1,start,end)

for _ in range(cases):
    order = tuple(map(int,stdin.readline().strip().split()))
    if order[0] == 1:
        update_seg_tree(1,start,end,order[1],order[2],order[3])
    else:
        print(xor_calc(1,start,end,order[1],order[2]))

'''
5
1 2 3 4 5
3
2 0 4
1 2 4 9
2 1 4
'''

'''
lazy를 쓰면 어느정도의 시간을 줄일 수 있을까?
'''