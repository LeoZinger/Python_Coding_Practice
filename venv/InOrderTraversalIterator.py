class TreeNode:
    def __init__(self, val:int):
        self.val = val
        self.left = None
        self.right = None

def inOrderTraverse(root):
    if root:
        inOrderTraverse(root.left)
        print(root.val)
        inOrderTraverse(root.right)

def iterInOrder(root):
    if root:
        stack = []
        # print("stack: ", stack)
        curr_node = root
    while stack or curr_node:
        if curr_node:
            # print("appendig curr node to stack: ", curr_node.val)
            stack.append(curr_node)
            # print("stack: ", stack)
            curr_node = curr_node.left
        else:
            curr_node = stack.pop()
            print("printing res Val ", curr_node.val)
            # if curr_node.right:
                # print("appendig curr.right node to stack: ", curr_node.right.val)
                # stack.append(curr_node.right)
            curr_node = curr_node.right

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
# inOrderTraverse(root)
iterInOrder(root)