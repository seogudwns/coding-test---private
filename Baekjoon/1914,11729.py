# https://www.acmicpc.net/problem/11729

n=int(input())

print(2**n-1) #실행횟수.

def hanoi(n,a,b,c):
    
    if n==1:
        return print(a,c)
    
    hanoi(n-1,a,c,b)
    print(a,c)
    hanoi(n-1,b,a,c)

hanoi(n,1,2,3) # 11729번

# if n<=20:
#     hanoi(n,1,2,3) # 1914번 