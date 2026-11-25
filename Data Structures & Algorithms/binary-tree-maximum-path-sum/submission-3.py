# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum=float("-inf")

        def dfs(node):
            nonlocal maxSum
            if node==None:
                return 0
            leftSum=dfs(node.left)
            rightSum=dfs(node.right)
            
            if leftSum<0:
                leftSum=0

            if rightSum<0:
                rightSum=0

            maxSum=max(maxSum,(leftSum+rightSum+node.val))

            return node.val+max(leftSum,rightSum)

        dfs(root)
        return maxSum
