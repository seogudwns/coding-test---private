# https://www.acmicpc.net/problem/1007
# L2 norm 계산..

# from sys import stdin

# def calc_dist(x,y):
#     return (x**2+y**2)**(1/2)

# def calc_total(lst,start,TF_lst,x,y):
#     # print('input :',lst,start,TF_lst,x,y)
#     if start == -1:
#         global dist
#         # print('x,y =',x,y)
#         dist = min(dist,calc_dist(x,y))
#         return
    
#     if dist == 0:
#         return
    
#     TF_lst[start] = True
#     for i in range(start+1,len(lst)):
#         if TF_lst[i] == False:
#             TF_lst[i] = True
#             z = -1
#             try:
#                 z = TF_lst.index(False)
#             except:
#                 pass
            
#             x_new = x + (lst[start][0]-lst[i][0])
#             y_new = y + (lst[start][1]-lst[i][1])
#             calc_total(lst,z,TF_lst,x_new,y_new)
            
#             x_new = x - (lst[start][0]-lst[i][0])
#             y_new = y - (lst[start][1]-lst[i][1])
#             calc_total(lst,z,TF_lst,x_new,y_new)
            
#             TF_lst[i] = False
    
#     TF_lst[start] = False
#     return

# cases = int(stdin.readline())
# dist = 0
# for _ in range(cases):
#     dots = [list(map(int,stdin.readline().strip().split())) for _ in range(int(stdin.readline()))]
    
#     dist = float('inf')
#     calc_total(dots,0,[False for _ in range(len(dots))],0,0)
    
#     print(dist)
    
# ! 계산으로 벡터를 더해주면 안되고, 마지막에 x,y에 대한 계산을 해줘야함... nono +인자와 -인자를 생각해보기.. n//2개의 +, n//2개의 -.


from sys import stdin
from itertools import combinations

cases = int(stdin.readline())
dist = 0
for _ in range(cases):
    x_lst = []
    y_lst = []
    leng = int(stdin.readline())
    for _ in range(leng):
        x,y = map(int,stdin.readline().strip().split())
        x_lst.append(x)
        y_lst.append(y)
    dist = float('inf')
    
    for i in combinations(range(leng),leng//2):
        xs,ys = 0,0
        for j in range(leng):
            if j in i:
                xs += x_lst[j]
                ys += y_lst[j]
            else:
                xs -= x_lst[j]
                ys -= y_lst[j]
                
        dist = min(dist,xs**2+ys**2)
        
    print(dist**(1/2))