class node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
def printing_inorder(root):
    if root is not None:
        printing_inorder(root.left) 
        print(root.val) 
        printing_inorder(root.right)
def printing_preorder(root):
    if root is not None:
        print(root.val) 
        printing_inorder(root.left) 
        printing_inorder(root.right)

def printing(root):
    if root==None:
        return
    printing(root.left)
    printing(root.right)
    print(root.val)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(4)
b=node(1)
print("inorder list is:")
printing_inorder(root)
print("preorder list is:")
printing_preorder(root)
print("postorder list is:")
printing(root)
