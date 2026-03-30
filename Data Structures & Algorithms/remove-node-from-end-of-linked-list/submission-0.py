# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        index = 0

        while curr:
            curr = curr.next
            index +=1
        curr = head

        if n == index:
            return head.next
        
        location = (index - n) -1
        counter = 0
        curr = head
        while counter < (location ):
            counter += 1
            curr = curr.next
        next_node = curr.next.next
        curr.next = next_node
        return head 