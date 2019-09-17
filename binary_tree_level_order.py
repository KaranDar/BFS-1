# Time Complexity : ?
# Space Complexity : ?
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        res, cur = [], [root]
        
        while cur:
            tmp, new = [], []

            for node in cur:
                tmp.append(node.val)
                if node.left is not None:
                    new.append(node.left)
                if node.right is not None:
                    new.append(node.right)
            res.append(tmp)
            cur = new
        
        return res
