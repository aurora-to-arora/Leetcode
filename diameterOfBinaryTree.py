# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]

        max_ht = {}
        d=0

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
            else:
                if node.left is None:
                    lht =0
                else:
                    lht=max_ht.pop(node.left)
                if node.right is None:
                    rht =0
                else:
                    rht=max_ht.pop(node.right)
                d = max(d, lht+rht)
                max_ht[node]=max(lht, rht)+1
        return d

                
