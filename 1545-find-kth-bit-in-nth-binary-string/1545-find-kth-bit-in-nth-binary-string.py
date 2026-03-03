class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = 2**n - 1
        mid = length // 2 + 1   
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            mirror = length - k + 1  
            v = self.findKthBit(n - 1, mirror)
            return "1" if v == "0" else "0"