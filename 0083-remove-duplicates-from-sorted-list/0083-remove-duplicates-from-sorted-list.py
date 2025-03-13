# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        nextnode=head
        while nextnode and nextnode.next:
            while nextnode and nextnode.next and nextnode.val==nextnode.next.val:
                nextnode.next=nextnode.next.next
            nextnode=nextnode.next
        return head