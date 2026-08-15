class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ml = float('-inf')
        bs = 0
        for i in range(n):
            low, high =i,i
            while low>=0 and high <n and s[low]==s[high]:
                l = high-low+1
                if l>= ml:
                    bs = low
                    ml = l
                low-=1
                high+=1
            
            low, high =i,i+1
            while low>=0 and high <n and s[low]==s[high]:
                l = high-low+1
                if l>= ml:
                    bs = low
                    ml = l
                low-=1
                high+=1
        return s[bs:ml+bs]
                
                    


                    
