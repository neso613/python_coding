class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert_left(self,value):
        if self.left is None:
            self.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = self.left
            self.left = new_node
            
    def insert_right(self,value):
        if self.right is None:
            self.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = self.right
            self.right = new_node

# Example usage:
root = TreeNode(1)
root.insert_left(2)
root.insert_right(3)

# Output the tree structure
print("Tree Structure:")
print("     ", root.value)
print("    /   \\")
print("  ", root.left.value, "   ", root.right.value)
