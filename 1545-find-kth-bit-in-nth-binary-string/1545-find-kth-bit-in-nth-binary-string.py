class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(bin1):
            bin2=""
            for i in bin1:
                if i=="0":
                    bin2+="1"
                else:
                    bin2+="0"
            return bin2
        
        def rev(bin1):
            return bin1[::-1]
        
        def recSn(n1):
            if n1==0:
                return "0"
            d=recSn(n1-1)
            return d+"1"+rev(invert(d))
        v=recSn(n)
        return v[k-1]