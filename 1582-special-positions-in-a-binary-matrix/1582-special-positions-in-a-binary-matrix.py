class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        l1 = [0]*n
        l2 = [0]*m

        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    l1[i]+=1
                    l2[j]+=1
        c=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    if (l1[i]==1 and l2[j]==1):
                        c+=1
        return c
                
