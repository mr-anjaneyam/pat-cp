from collections import deque

class TreeNode:
    def init(self,value):
        self.val=value
        self.left=None
        self.right=None
        
def reverse_level_order(root):
    if not root:
        return []
    
    result=[]
    queue=deque([root])
    
    while queue:
        level_size=len(queue)
        current_level=deque()
        
        for _ in range(level_size):
            node=queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    result.insert(0,current_level)#Insert current level list at the beginning 
        
#Driver Code
if __name__=='__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(7)
    
#Perform level order traversal in spiral form
rev_order=reverse_level_order(root)
print("Level order traversal in reverse order form:",rev_order)