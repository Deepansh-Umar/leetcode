class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        minlen = float("inf")
        minstr = ""
        digits = [int(_) for _ in s]
        n = len(digits)
        i,s1=0,0
        for j, val in enumerate(digits):
            s1+=val
            while(s1>=k and i<=j):
                if(s1==k):
                    if (j-i+1 < minlen or(j-i+1 == minlen and (minstr == "" or s[i:j+1] < minstr))):
                        minlen = j-i+1
                        minstr = s[i:j+1]
                s1-=digits[i]
                i+=1
        return minstr
