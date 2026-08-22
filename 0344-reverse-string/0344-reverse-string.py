class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l,h = 0, n-1
        while(l<=h):
            temp = s[l]
            s[l] = s[h]
            s[h] = temp
            l+=1
            h-=1
        