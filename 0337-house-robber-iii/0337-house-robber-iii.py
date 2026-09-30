# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        
        return max(self.solve(root))

    def solve(self, node):
        if(not node):
            return [0,0]
        if(not node.left and not node.right):
            return [node.val,0]
        left = self.solve(node.left)
        right = self.solve(node.right)
        torob = node.val + left[1]+right[1]
        tonotrob = max(left)+max(right)
        return [torob,tonotrob]