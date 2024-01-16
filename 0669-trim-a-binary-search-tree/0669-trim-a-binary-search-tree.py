# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trav(curr):
            if curr==None:
                return None
            
            if curr.val<low:
                temp = trav(curr.right)
                return temp
            elif curr.val>high:
                temp = trav(curr.left)
                return temp

            curr.left = trav(curr.left)
            curr.right = trav(curr.right)

            return curr
        
        dummy=TreeNode(0,None,root)
        dummy.right = trav(dummy.right)
        return dummy.right

            
