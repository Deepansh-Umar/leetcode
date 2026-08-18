class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #creating frequency maps of both strings
        shs = Counter(s)
        ths = Counter(t)

        #initial compare for missing characters
        if len(shs)!=len(ths): return False
        for i in ths:
            #comparision of frequecny of each character
            if i not in shs or shs[i]!=ths[i]:
                return False
        return True