class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        k = n
        if(n<1000):
            return res
        while(n>=1000):
            res+=1
            n/=1000
        return res*(k-999)