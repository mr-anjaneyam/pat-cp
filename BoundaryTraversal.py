from collections import deque

class TreeNode:
    def init(self,value):
        self.val=value
        self.left=None
        self.right=None
        
def print_leaves(root, result):
    if root:
        print_leaves(root.left, result)
        if not root.left and not root.right:
            result.append(root.val)
        print_leaves(root.right, result)

def print_left_boundary(root, result):
    if root:
        if root.left:
            result.append(root.val)
            print_left_boundary(root.left, result)
        elif root.right:
            result.append(root.val)
            