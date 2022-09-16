from sys import stdin

num = int(stdin.readline())

sentences = []
last = []

for _ in range(num):
    arr = stdin.readline().strip().split()
    sentences.append(arr)
    last.append(len(arr))

start = [0 for _ in range(len(last))]
aim = stdin.readline().strip().split()

if sum(last) != len(aim):
    print('Impossible')
    exit(0)
    
for i in aim:
    tmp = 0
    for j in range(num):
        curr = start[j]
        if curr == last[j]:
            continue
        if sentences[j][curr] == i:
            start[j] += 1
            tmp = 1
            break
    # print(i,j,start[j])
    if tmp == 0:
        print('Impossible')
        exit(0)
        
print('Possible')

# ! 16번째 줄 : sum(last) > len(aim) 이어도 정답.. but < 일 경우 오답. last로 모든 단어가 채워졌는데 aim에 그 뒤에 단어가 있을 수 있기 때문.
