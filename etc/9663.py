N = int(input())

# lst = [0,1,0,0,]
# lst[8] = 92

chess_board = [[1 for _ in range(N)] for _ in range(N)]

def change_false(board,i,j):
        
    for k in range(N): # 행렬 바꿈.
        board[i][k] = 0
        board[k][j] = 0
    
    tmp = i+j
    for k in range(tmp+1): # y=x 바꿈.
        board[tmp-k][k] = 0
        
    tmp = abs(i-j)
    x,y = (0,tmp) if i>j else (tmp,0) 
    for k in range(tmp-1,N-tmp): # y=-x 바꿈.
    #     print(y+k,x+k)
        board[y+k][x+k] = 0
    
    
result = 0
for i in range(N):
    1
