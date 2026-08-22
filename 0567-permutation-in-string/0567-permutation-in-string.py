from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_zero(d):
            for key in d:
                if d[key]>0:
                    return False
            return True
        og = Counter(s1)
        c = Counter(s1)
        n = len(s2)
        m = len(s1)
        if(n<m):
            return False
        i,j = 0,0
        while(i<=j and j<n):
            if(j-i < m):
                k = s2[j]
                if( k in c and c[s2[j]]>0):
                    c[s2[j]]-=1
                    j+=1
                elif(k not in c):
                    j+=1
                    i=j
                    c = copy.deepcopy(og)
                else:
                    
                    c[s2[i]]+=1
                    i+=1
                    
            elif(j-i == m):
                if(is_zero(c)):
                    return True
                else:
                    j+=1
                    c[s2[i]]+=1
                    i+=1
        if(is_zero(c)):
            return True
        return False