# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        start = head
        length = 0
        while(start != None):
            start = start.next
            length += 1
        
        ground = head
        prev = head
        current = head.next
        next_step = current.next
        prior = None

        for i in range(length//k):
            for j in range(k-1):
                current.next = prev    
                prev = current
                current = next_step
                if next_step != None:
                    next_step = next_step.next
        
            ground.next = current
            if i == 0:
                head = prev
            else:
                prior.next = prev
            if i != length//k-1:
                prior = ground
                prev = current
                ground = current
                current = current.next
                next_step =  current.next
        return head


            
