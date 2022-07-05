class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def addNode(root, val):
    if root is None:
        root = BinaryTreeNode(val)
        return root
    if val < root.val:
        root.left = addNode(root.left, val)
    else:
        root.right = addNode(root.right, val)
    return root

def inorderTraversal(root):
    if not root:
        return
    if root.left:
        inorderTraversal(root.left)
    print(root.val, end=' ')
    if root.right:
        inorderTraversal(root.right)

def searchBSTTree(root, n):
    if not root:
        return False

    res = False
    if n == root.val:
        return True
    if n < root.val:
        res = searchBSTTree(root.left, n)
    else:
        res = searchBSTTree(root.right, n)
    return res

bst = addNode(None, 5)
bst = addNode(bst, 6)
bst = addNode(bst, 4)
bst = addNode(bst, 3)
bst = addNode(bst, 7)

print("BST InOrderTraversal: ")
inorderTraversal(bst)
print("\n")
print("searchBSTTree(5) = ", searchBSTTree(bst, 5))