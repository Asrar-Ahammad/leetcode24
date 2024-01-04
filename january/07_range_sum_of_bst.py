class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traversal(root):
        tree = []
        if root != None:   
            tree.append(root.val)
        if root:
            traversal(root.left)
            tree.append(root.val)
            traversal(root.right)
        return tree

class Solution:
    def rangeSumBST(self, root:[TreeNode], low: int, high: int) -> int:
        tree = traversal(root)
        print(tree)
        sum = 0
        for i in tree:
            if low<=i<=high:
                sum+=i
        return sum