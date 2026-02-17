class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def bincount(n):
            b = bin(n)
            return b.count('1')
        bl=[]
        for i in range(12):
            for j in range(60):
                if turnedOn == bincount(i)+bincount(j):
                    rs = str(i) + ":"
                    if j<10:
                        j = "0"+str(j)
                    rs+= str(j)
                    bl.append(rs)
        return bl
             
                