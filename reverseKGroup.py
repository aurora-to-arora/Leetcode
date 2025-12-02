# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseNode(node):
            prev = None 
            current = node
            while current:
                nxt = current.next
                current.next = prev
                prev= current
                current = nxt
            return prev

        dummy  = ListNode(-1, head)
        current = dummy

        while True:
            kth = current
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            start = current.next
            end = kth.next

            kth.next = None

            new_head=reverseNode(start)
            current.next = new_head
            start.next = end

            current = start
