class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
        
def print_leaves(root,result):
    if root:
        print_leaves(root.left,result)
        if not root.left and not root.right:
            result.append(root.val)
        print_leaves(root.right,result)
        
def print_left_boundary(root,result):
    if root:
        if root.left:
            result.append(root.val)
            print_left_boundary(root.left,result)
        elif root.right:
            result.append(root.val)
            print_left_boundary(root.left,result)
def print_right_boundary(root,result):
    if root:
        if root.right:
            print_right_boundary(root.right,result)
            result.append(root.val)
        elif root.left:
            print_right_boundary(root.left,result)
            result.append(root.val)
            
def boundary_traversal(root):
    if not root:
        return []
    
    result=[root.val]
    
    #Print left boundary (excluding the root if it has a right child)
    print_left_boundary(root.left,result)
    
    #Print leaf nodes
    print_leaves(root,result)
    
    #Print right boundary (excluding the root if it has a left child)
    print_right_boundary(root.right,result)
    
    return result

#Example usage
#Constructing a binary tree with different data
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
root.left.right.left=TreeNode(5)
root.left.right.right=TreeNode(6)
root.right.left=TreeNode(7)
root.right.right=TreeNode(8)

boundary_order=boundary_traversal(root)
print("Boundary Traversal of the binary tree:",boundary_order)