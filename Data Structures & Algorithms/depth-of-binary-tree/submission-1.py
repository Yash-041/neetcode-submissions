# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root == None:
        #     return 0
        # leftHeight=self.maxDepth(root.left)
        # rightHeight=self.maxDepth(root.right)

        # return 1+max(leftHeight,rightHeight)
        if not root:
            return 0
        queue=deque()
        height=0
        queue.append(root)
        while queue:
            height+=1
            level_size=len(queue)
            for _ in range(level_size):
                e=queue.popleft()
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
                
        return height
    