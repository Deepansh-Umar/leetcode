class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=0
        if not a or not b:
            return a+b
        n1 = len(a)-1
        n2 = len(b)-1
        if n1>n2:
            b = "0"*(n1-n2)+b
        else:
            a="0"*(n2-n1)+a
        rs = ''
        n1=len(a)-1
        while n1>=0:
            v = (int(a[n1])+int(b[n1]))+c
            if v==2:
                c=1
                v=0
            elif v==3:
                c=1
                v=1
            else:
                c=0
            rs = str(v)+rs
            n1-=1
            if c>0 and (n1==-1):
                rs= str(c)+rs
        return rs
