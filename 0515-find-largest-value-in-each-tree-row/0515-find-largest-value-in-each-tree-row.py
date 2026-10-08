# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        d = {}        
        self.recur(root,0,d)
        arr = [d[i] for i in range(len(d))]
        return arr
        
    def recur(self,node,level,d):
        if not node:
            return
        if(level in d):
            d[level] = max(d[level], node.val)
        else:
            d[level] = node.val
        
        self.recur(node.left, level+1,d)
        self.recur(node.right,level+1,d)