from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def SpiralLevelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level_size = len(queue)
        current_level = deque()
        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(current_level))
        left_to_right = not left_to_right
    return result

#Driver Code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print("Spiral Order Traversal of the given tree is : ", SpiralLevelOrder(root))