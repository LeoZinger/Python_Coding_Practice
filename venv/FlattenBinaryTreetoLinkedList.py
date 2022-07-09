from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root: TreeNode) -> TreeNode:
            if not root:
                return None
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            # flatten left tree into right tree
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            last = rightTail or leftTail or root
            return last

        dfs(root)


solution = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

res = solution.flatten(root)

print("Flatted linked list: \n")
while root:
    print(root.val, end=",")
    root = root.right
