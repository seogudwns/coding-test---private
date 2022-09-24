# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []
            
        results = []
        Q = deque([(root,targetSum,[])])
        
        while Q:
            node,res,lst = Q.popleft()
            if not (node.left or node.right):
                if node.val == res:
                    results.append(lst+[node.val])
                continue
            
            if node.left:
                Q.append((node.left,res-node.val,lst+[node.val]))
            if node.right:
                Q.append((node.right,res-node.val,lst+[node.val]))
            
        return results
    # ! Caution : node.val이 항상 양수인 것은 아니다.. 음수인 경우도 있음.
    
'''
result :
Runtime: 49 ms, faster than 90.03% of Python3 online submissions for Path Sum II.
Memory Usage: 15.4 MB, less than 89.27% of Python3 online submissions for Path Sum II.
'''