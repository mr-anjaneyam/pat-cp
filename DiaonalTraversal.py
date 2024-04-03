from collections import deque
def diagonalTraversal(root):
    if not root:
        return []
    result = []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()
        if level == len(result):
            result.append([])
        result[level] += [node.val]
        if node.left:
            queue.append((node.left, level+1))
        if node.left:
            queue.append((node.left, level))

    return result

#Driver Code
if __name__=='__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(7)

diagonal_order = diagonalTraversal(root)
print("diagonal traversal is", diagonal_order)
