# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        r = ListNode()
        d = r
        while l1 or l2 or carry:
            v=0
            if l1:
                v+=l1.val
                l1=l1.next
            if l2:
                v+=l2.val
                l2=l2.next
            v+=carry
            if v>9 :
                carry = v//10
                v = v%10
            else:
                carry = 0
            
            d.next = ListNode(v)
            d=d.next
            
        return r.next
            