# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use two pointers: slow moves 1 step, fast moves 2 steps.
        # If there is a cycle, fast will eventually meet slow.
        # If fast reaches None, there is no cycle.

        slow = head 
        fast = head 

        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast:
                return True 

        return False 
        