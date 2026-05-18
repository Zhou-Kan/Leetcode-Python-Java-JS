class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    if not preorder or not inorder:
        return None
    
    node_val = preorder[0]
    idx = inorder.index(node_val)
    size = idx
    node = TreeNode(node_val)
    node.left = build_tree()
    
    
