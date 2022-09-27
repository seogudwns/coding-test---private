# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        domino_split = ['.']
        LR_idx = []
        for i in range(n):
            domino_split.append(dominoes[i])
            if dominoes[i] == 'L':
                LR_idx.append((i+1,'L'))
            elif dominoes[i] == 'R':
                LR_idx.append((i+1,'R'))

        domino_split.append('.')
        
        if not LR_idx:
            return dominoes
        
        elif len(LR_idx) == 1:
            if LR_idx[0][1] == 'L':
                for i in range(1,LR_idx[0][0]):
                    domino_split[i] = 'L'
            else:
                for i in range(LR_idx[0][0]+1,n+1):
                    domino_split[i] = 'R'
            
            return ''.join(domino_split[1:-1])
        
        
        if LR_idx[0][1] == 'L':
            for i in range(1,LR_idx[0][0]):
                domino_split[i] = 'L'
        else:
            if LR_idx[1][1] == 'L':
                left = LR_idx[0][0]
                right = LR_idx[1][0]
                while True:
                    if right-left<=2:
                        break
                    left+=1
                    right-=1
                    domino_split[left] = 'R'
                    domino_split[right] = 'L'
            else:
                for i in range(LR_idx[0][0]+1,LR_idx[1][0]):
                    domino_split[i] = 'R'
        
        for i in range(1,len(LR_idx)-1):
            if LR_idx[i][1] == 'R':
                if LR_idx[i+1][1] == 'L':
                    left = LR_idx[i][0]
                    right = LR_idx[i+1][0]
                    
                    while True:
                        if right-left<=2:
                            break
                        left+=1
                        right-=1
                        domino_split[left] = 'R'
                        domino_split[right] = 'L'
                
                elif LR_idx[i+1][1] == 'R':
                    for j in range(LR_idx[i][0]+1,LR_idx[i+1][0]):
                        domino_split[j] = 'R'
            
            else: # LR_idx[i][1] == 'L'
                if LR_idx[i-1][1] == 'R':
                    continue
                    
                for i in range(LR_idx[i-1][0]+1,LR_idx[i][0]):
                    domino_split[i] = 'L'
        
        if LR_idx[-1][1] == 'R':
            for i in range(LR_idx[-1][0]+1,n+1):
                domino_split[i] = 'R'
        else:
            if LR_idx[-2][1] == 'L':
                for i in range(LR_idx[-2][0]+1,LR_idx[-1][0]):
                    domino_split[i] = 'L'
        
        return ''.join(domino_split[1:-1])
    
# easy method..

# class Solution:
#     def pushDominoes(self, dominoes: str) -> str:
#         temp = ''
        
#         while dominoes != temp:
#             temp = dominoes
#             dominoes = dominoes.replace('R.L', 'xxx')
#             dominoes = dominoes.replace('R.', 'RR')
#             dominoes = dominoes.replace('.L', 'LL')

#         return  dominoes.replace('xxx', 'R.L')