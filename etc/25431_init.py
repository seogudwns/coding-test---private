from sys import stdin

N =  int(stdin.readline().strip())
lst = [0]+list(map(int,stdin.readline().strip().split()))
Q = int(stdin.readline().strip())

def get_min(start,end,num):
    result = start
    tmp = num^lst[start]
    for i in range(start+1,end+1):
        xor_num = num^lst[i]
        if xor_num < tmp:
            result = i
            tmp = xor_num
        elif xor_num == tmp and lst[i]<lst[result]:
            result = i
    
    return result
    
def get_max(start,end,num):
    result = start
    tmp = num^lst[start]
    for i in range(start+1,end+1):
        xor_num = num^lst[i]
        if xor_num > tmp:
            result = i
            tmp = xor_num
        elif xor_num == tmp and lst[i]<lst[result]:
            result = i
    
    return result

for _ in range(Q):
    arr = tuple(map(int,stdin.readline().strip().split()))
    
    if arr[0] == 1:
        print(get_min(arr[1],arr[2],arr[3]))
    elif arr[0] == 2:
        print(get_max(arr[1],arr[2],arr[3]))
    else:
        lst[arr[1]] = arr[2]

# ! inital code.. 더 효율적인 방법을 찾을 필요가 있다... segtree? 