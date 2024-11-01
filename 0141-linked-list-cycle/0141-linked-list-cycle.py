# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        l=[]
        while(head):
            if head.next not in l:
                l.append(head.next)
            else:
                return True
            head=head.next
        return False
        