# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if(root == None):
            return 0
        q = [root]
        l =0 
        while(q):
            n = len(q)
            for i in range(n):
                v = q.pop(0)
                if(v.left):
                    q.append(v.left)
                if(v.right):
                    q.append(v.right)
            l+=1
        return l
            
            
