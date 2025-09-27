# implementation of binary search tree using array with preorder traversal, inorder traversal and postorder traversal recursively.

class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        
def preorder(root):
    if root is None:
        return []
    
    res = []
    res.append(root.key)
    res.extend(preorder(root.left))
    res.extend(preorder(root.right))
    return res        
        
def inorder(root):
    if root is None:
        return []
    
    res = []
    res.extend(inorder(root.left))
    res.append(root.key)
    res.extend(inorder(root.right))
    return res

def postorder(root):
    if root is None:
        return []
    
    res = []
    res.extend(postorder(root.left))
    res.extend(postorder(root.right))
    res.append(root.key)
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

'''
          1
         / \
       2     3
      / \   / \
     4  5  6   7

'''

# Demonstrate all three traversals
preorder_result = preorder(root)
print("Preorder traversal: ", preorder_result)

inorder_result = inorder(root)
print("Inorder traversal: ", inorder_result)

postorder_result = postorder(root)
print("Postorder traversal: ", postorder_result)
