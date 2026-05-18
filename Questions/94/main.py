class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: ListNode | None) -> list[int]:
    ans = []
    if not root:
        return ans
    
    def dfs(root: ListNode | None) -> None:
        if not root:
            return 
        
        dfs(root.left)
        ans.append(root.val)
        dfs(root.right)
    
    dfs(root)
    return ans

node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node1.left = node2
node1.right = node3
print(inorder_traversal(node1))