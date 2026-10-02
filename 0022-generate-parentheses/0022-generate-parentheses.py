class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def addpar(op, cl):

            if op==cl==n:
                res.append(''.join(stack))
                return
            if op<n:
                stack.append('(')
                addpar(op+1,cl)
                stack.pop()
            if cl < op:
                stack.append(')')
                addpar(op,cl+1)
                stack.pop()
            
        addpar(0,0)
        return res