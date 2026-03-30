# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None 
        curr = slow
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        first = head
        second = prev
        while first and second:
            first_next_node = first.next
            second_next_node = second.next

            first.next = second

            if first_next_node is None:
                break
            second.next = first_next_node


            second = second_next_node
            first = first_next_node      