# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        result1 = 0
        for i in arr1:
            result1 ^= i
        
        result2 = 0
        for i in arr2:
            result2 ^= i
            
        return result1 & result2
        
# [1,2,5,7,818]
# [123,34]
# output : 819.. Expected : 17?

# (a&b) ^ (a&c) ^ (a&d) ?= a&(b^c^d)
# ((a&b) ^ (a&c)) ^ (a&d) == a&(b^c) ^ a&d = a&((b^c)^d)
