# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        sol=[]
        q=[root]
        i=0
        while q:
            n=len(q)
            l=[0]*n
            if i%2==0:
                for _ in range(n):
                    curr=q.pop(0)
                    l[_]=curr.val
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)

            else:
                for _ in range(n-1,-1,-1):
                    curr=q.pop(0)
                    l[_]=curr.val
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            i+=1
            sol.append(l)
        return sol
