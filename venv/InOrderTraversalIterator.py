from typing import List

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

def iterPreOrder(root):
    if root:
        stack = []
        # print("stack: ", stack)
        curr_node = root
    print("iterPreOrder:", end=" ")
    while stack or curr_node:
        if curr_node:
            print(curr_node.val, end=" ")
            # print("appendig curr node to stack: ", curr_node.val)
            stack.append(curr_node.right)
            curr_node = curr_node.left
            # print("stack: ", stack)
        else:
            curr_node = stack.pop()
            # print("appendig curr.right node to stack: ", curr_node.right.val)
                # stack.append(curr_node.right)

class IterateInOrder:
    def __init__(self, root: TreeNode):
        self.curr_node = root
        self.stack = []

    def hasNext(self) -> bool :
        if self.stack or self.curr_node:
            return True
        else:
            return False

    def next(self) -> TreeNode:
        ret_node = TreeNode(0)
        while self.curr_node:
            self.stack.append(self.curr_node)
            self.curr_node = self.curr_node.left

        if not self.curr_node:
            self.curr_node = self.stack.pop()
            ret_node = self.curr_node
            self.curr_node = self.curr_node.right

        return ret_node

def findTreeHeight(node: TreeNode) -> int:
    if not node:
        return 0
    return max(findTreeHeight(node.left)+1, findTreeHeight(node.right)+1)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Height of tree = ", findTreeHeight(root))

# inOrderTraverse(root)
# iterInOrder(root)
iterPreOrder(root)

iterateInOrder = IterateInOrder(root)
print("Next:", end=" ")
while iterateInOrder.hasNext():
    curr_node = iterateInOrder.next()
    print(curr_node.val, end=" ")
