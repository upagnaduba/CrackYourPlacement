# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sol=[]
        if root is None:
            return sol
        q=[root]
        while q:
            s=0
            n=len(q)
            for _ in range(n):
                curr=q.pop(0)
                s+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            sol.append(s/n)
        return sol