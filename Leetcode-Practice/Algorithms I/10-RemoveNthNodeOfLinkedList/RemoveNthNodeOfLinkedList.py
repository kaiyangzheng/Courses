# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def twoPass_removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 1
        while(current.next != None):
            current = current.next;
            length += 1
        if length == 1:
            head = None;
            return head;
        if length-n-1 < 0:
            head = head.next
            return head
        current = head
        for i in range(length-n-1):
            current = current.next
        current.next = current.next.next
        return head
    
    

