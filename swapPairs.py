# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode('start', head)

        while current.next != None and current.next.next!= None:
            first = current.next
            second = current.next.next

            first.next = second.next
            current.next = second
            current.next.next= first

            current = first
        return dummy.next
