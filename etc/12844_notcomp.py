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

# from sys import stdin

# end = int(stdin.readline().strip())
# start = 0
# lst = list(map(int,stdin.readline().strip().split()))

# cases = int(stdin.readline().strip())

# seg_tree = [None]*(4*end)
# lazy = [0]*(4*end)   
# # --> 요걸 이용해야함..  2번 명령에서 바뀌는 부분은 바뀌고 이후에 바뀌어도 될 것은 lazy에 저장(start,end와 관계없이 저장, 
# # 적용은 1번에서 쓸 때.), 필요시 바꾸는 연산을 진행해야함. 
# # 1번 명령에서도 lazy가 있을 시 필요한 부분만 적용시키고 다시 나머지는 lazy에 저장.
# end -= 1

# def make_seg_tree(idx,start,end):
#     if start == end:
#         seg_tree[idx] = lst[start]
#         return seg_tree[idx]
    
#     mid = (start+end)//2
#     seg_tree[idx] = make_seg_tree(2*idx,start,mid) ^ make_seg_tree(2*idx+1,mid+1,end)
#     return seg_tree[idx]


# def update_seg_tree(idx,start,end,update_start,update_end,num):
#     # print('update_check :',idx,start,end,update_start,update_end) # done.
#     # print(min(update_end,end),max(update_start,start))  # update 범위가 애매하게 겹칠 때를 고려할 필요가 있음.
#     if update_end<start or end<update_start:  # 바뀌는 범위에 완전히 벗어나는 케이스.
#         return
#     elif (min(update_end,end)-max(update_start,start))%2 == 0: # xor이기 때문에 짝수번 연산이 되는 것은 없는 것과 동일. start == end일 경우 가장 기본 원소가 들어가고, 홀수의 경우(ex start : 2, end : 4 인 경우 2,3,4로 홀수 갯수.) (end-start)%2 == 0 이 성립.
#         # print('update_change :',idx,start,end)  
#         seg_tree[idx] ^= num
#         if start == end:
#             return

#     mid = (start+end)//2
#     update_seg_tree(2*idx,start,mid,update_start,update_end,num)
#     update_seg_tree(2*idx+1,mid+1,end,update_start,update_end,num)
#     return

# def xor_calc(idx,start,end,calc_start,calc_end):
#     # print('xor_calc input :',idx,start,end,calc_start,calc_end)
#     if calc_start>end or calc_end<start:
#         return 0
    
#     mid = (start+end)//2
#     if calc_start<=start and end<=calc_end:
#         # print('calc :',seg_tree[idx],'& start,end : ',start,end)
#         return seg_tree[idx]
    
#     return xor_calc(2*idx,start,mid,calc_start,calc_end)^xor_calc(2*idx+1,mid+1,end,calc_start,calc_end)

# make_seg_tree(1,start,end)

# for _ in range(cases):
#     order = tuple(map(int,stdin.readline().strip().split()))
#     if order[0] == 1:
#         update_seg_tree(1,start,end,order[1],order[2],order[3])
#     else:
#         print(xor_calc(1,start,end,order[1],order[2]))

# ! lazy를 적용시키기 전 code

# from sys import stdin

# end = int(stdin.readline().strip())
# start = 0
# lst = list(map(int,stdin.readline().strip().split()))

# cases = int(stdin.readline().strip())

# seg_tree = [0]*(4*end)
# lazy = [0]*(4*end)   
# # --> 요걸 이용해야함..  2번 명령에서 바뀌는 부분은 바뀌고 이후에 바뀌어도 될 것은 lazy에 저장(start,end와 관계없이 저장, 
# # 적용은 1번에서 쓸 때.), 필요시 바꾸는 연산을 진행해야함. 
# # 1번 명령에서도 lazy가 있을 시 필요한 부분만 적용시키고 다시 나머지는 lazy에 저장.
# end -= 1 # len(lst) = end --> lst[end-1]이 마지막 원소.

# def make_seg_tree(idx,start,end):
#     if start == end:
#         seg_tree[idx] = lst[start]
#         return seg_tree[idx]
    
#     mid = (start+end)//2
#     seg_tree[idx] = make_seg_tree(2*idx,start,mid) ^ make_seg_tree(2*idx+1,mid+1,end)
#     return seg_tree[idx]


# def update_seg_tree(idx,start,end,update_start,update_end,num):
#     # print('update input :',idx,start,end,update_start,update_end,num)
#     if lazy[idx]:
#         num ^= lazy[idx]
#         lazy[idx] = 0

#     if update_end<start or end<update_start:
#         return
#     elif (min(update_end,end)-max(update_start,start))%2 == 0:
#         seg_tree[idx] ^= num
#         if start == end:
#             return

#     if update_start<=start and end<=update_end and start != end:
#         # print(idx,start,end,update_start,update_end,num) # !!! check용.
#         lazy[2*idx] ^= num
#         lazy[2*idx+1] ^= num
#         return
    
#     mid = (start+end)//2
#     update_seg_tree(2*idx,start,mid,update_start,update_end,num)
#     update_seg_tree(2*idx+1,mid+1,end,update_start,update_end,num)
#     return

# def xor_calc(idx,start,end,calc_start,calc_end):
#     # print('xor_calc input :',idx,start,end,calc_start,calc_end)
#     if calc_start>end or calc_end<start:
#         return 0
    
#     if lazy[idx]:
#         update_seg_tree(idx,start,end,calc_start,calc_end,lazy[idx])
        
#     mid = (start+end)//2
#     if calc_start<=start and end<=calc_end:
#         # print('calc :',seg_tree[idx],'& start,end : ',start,end)
#         return seg_tree[idx]
    
#     return xor_calc(2*idx,start,mid,calc_start,calc_end)^xor_calc(2*idx+1,mid+1,end,calc_start,calc_end)

# make_seg_tree(1,start,end)

# for _ in range(cases):
#     order = tuple(map(int,stdin.readline().strip().split()))
#     if order[0] == 1:
#         update_seg_tree(1,start,end,order[1],order[2],order[3])
#     else:
#         print(xor_calc(1,start,end,order[1],order[2]))

# ! lazy를 썼는데 틀림.. 추정으로는 calc에서 lazy를 적용시킬때 틀린듯.
# ! 틀림2.. index error인데 어디서 나오는거지.. 아예 update와 calc를 다시 짜보자. 

from sys import stdin

end = int(stdin.readline().strip())
start = 0
lst = list(map(int,stdin.readline().strip().split()))

cases = int(stdin.readline().strip())

seg_tree = [0]*(4*end)
lazy = [0]*(4*end)
# # --> 요걸 이용해야함..  2번 명령에서 바뀌는 부분은 바뀌고 이후에 바뀌어도 될 것은 lazy에 저장(start,end와 관계없이 저장, 
# # 적용은 1번에서 쓸 때.), 필요시 바꾸는 연산을 진행해야함. 
# # 1번 명령에서도 lazy가 있을 시 필요한 부분만 적용시키고 다시 나머지는 lazy에 저장.
end -= 1 # len(lst) = end --> lst[end-1]이 마지막 원소.

def make_seg_tree(idx,start,end):
    if start == end:
        seg_tree[idx] = lst[start]
        return seg_tree[idx]
    
    mid = (start+end)//2
    seg_tree[idx] = make_seg_tree(2*idx,start,mid) ^ make_seg_tree(2*idx+1,mid+1,end)
    return seg_tree[idx]


def update_seg_tree(idx,start,end,update_start,update_end,num):
    # print('update input :',idx,start,end,update_start,update_end,num)
    if lazy[idx]: # [start,end] 범위 전체에 업데이트 할 것이 남아있다는 말.
        num ^= lazy[idx]
        lazy[idx] = 0

    if update_end<start or end<update_start:
        return
    
    # else := update_start <= start or end <= update_end.
    if start == end:  #calc leaf of the seg_tree.
        seg_tree[idx] ^= num
        # print('idx update1 :',idx,num,start)
        return
    elif start<=update_start and update_end<=end: #탐색 bound가 업데이트할 bound를 품은 경우.
        if (update_end-update_start)%2 == 0:
            # print('idx update2 :',idx,num,start,end)
            seg_tree[idx] ^=num
    elif update_start <= start and end <= update_end: #탐색 bound가 업데이트할 bound에 품어져있는 경우.
        if (end-start)%2 == 0:
            # print('idx update3 :',idx,num,start,end)
            seg_tree[idx] ^=num
        # seg_tree에 대한 update가 필요할 경우 update, 그 아래는 child의 변화는 lazy에 보관.
        lazy[2*idx] ^= num
        lazy[2*idx+1] ^= num
        return

    mid = (start+end)//2
    
    update_seg_tree(2*idx,start,mid,update_start,update_end,num)
    update_seg_tree(2*idx+1,mid+1,end,update_start,update_end,num)
    return

def xor_calc(idx,start,end,calc_start,calc_end):
    # print('xor_calc input :',idx,start,end,calc_start,calc_end)
    if calc_start>end or calc_end<start:
        return 0
    
    if lazy[idx]:
        update_seg_tree(idx,start,end,calc_start,calc_end,lazy[idx]) 
        # lazy[idx] = 0 on inner stack, calc_start와 calc_end 사이에 계산되야 할 것을 다 계산하기.
    
    if calc_start <= start and end <= calc_end:
        return seg_tree[idx]
    
    mid = (start+end)//2
    return xor_calc(2*idx,start,mid,calc_start,calc_end)^xor_calc(2*idx+1,mid+1,end,calc_start,calc_end)

make_seg_tree(1,start,end)

# print(seg_tree)

for _ in range(cases):
    order = tuple(map(int,stdin.readline().strip().split()))
    if order[0] == 1:
        update_seg_tree(1,start,end,order[1],order[2],order[3])
        # print(seg_tree)
        # print(lazy)
    else:
        print(xor_calc(1,start,end,order[1],order[2]))
        # print(seg_tree)
        # print(lazy)

# ! lazy의 정의를 명확하게 할 필요가 있다.. 그냥 계산이 되야하는게 아니고, start와 end에 묶여있는 것만 남겨야한다. 
# ! ex. 3~4에 남아있는데 2~3을 구할 때는 3~4가 쪼개지지 않고, 따라서 게산되지 않음. --> 계산되는데..?.. 
# ! 0~4 --> (0~2 --> 2~2 return, 3~4 --> update : 3~4, 3~3, 4~4 & after return 3~3.)
# TODO : 틀리는 이유를 찾아보자!!!

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