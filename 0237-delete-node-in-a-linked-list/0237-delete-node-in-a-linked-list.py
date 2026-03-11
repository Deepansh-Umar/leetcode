# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        temp = node.next
        while temp:
            node.val = temp.val
            prev = node
            node = temp
            temp = temp.next
        prev.next= None
        