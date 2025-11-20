# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def backtrack(node, count):
            if not node:
                return
            if len(res)==count:
                res.append([])
            res[count].append(node.val)
            backtrack(node.left,count+1)
            backtrack(node.right,count+1)
        backtrack(root, 0)
        return res


        
