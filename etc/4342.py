# https://www.acmicpc.net/problem/4342
        
# from sys import stdin

# while True:
#     a,b = map(int,stdin.readline().strip().split())
#     if a == 0:
#         break
#     elif a<b:
#         a,b = b,a
    
#     if b<a<2*b: # 반례.. 19 15. 
#         while True:
#             a,b = a%b,b%a
#             print(a,b)
#             if a == 0:
#                 print('A wins')
#                 break
            
#             elif b == 0:
#                 print('B wins')
#                 break
            
#     else:
#         print('A wins')

from sys import stdin

def gcd(a,b):
    if a%b == 0:
        return True
    elif a-b<b:
        return False if gcd(b,a-b) else True
    else:
        return True

while True:
    a,b = map(int,stdin.readline().strip().split())
    if a == 0:
        break
    elif a<b:
        a,b = b,a
    
    if gcd(a,b):
        print('A wins')
    else:
        print('B wins')