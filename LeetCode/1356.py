class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def get_bit_num(num):
            result = 0
            for i in range(14):
                if num & (1<<i):
                    result += 1
            return result
        
        return sorted(arr,key=lambda x: (get_bit_num(x),x))