# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = False
        if not head:
            return None
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                f=True
                break
        if f:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow
        return None