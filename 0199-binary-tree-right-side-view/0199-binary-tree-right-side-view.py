# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        sol=[]
        if root is None:
            return sol
        q=[root]
        while q:
            sol.append(q[-1].val)
            for i in range(len(q)):
                curr=q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return sol
                        