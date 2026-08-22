class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        s1 = "".join(sorted(list(s1)))
        for i in range(n-m+1):
            ns = s2[i:i+m]
            ns= "".join(sorted(list(ns)))
            if ns==s1:
                return True
        return False