# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        if not head:
            return None
        temp = curr
        while temp:
            curr = temp
            temp = curr.next
            curr.next = prev
            prev = curr
        return curr

