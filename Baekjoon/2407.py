n,m = map(int,input().split())

result = 1
div = 1
for i in range(1,m+1):
    result *= n-i+1
    div *= i

print(result//div)