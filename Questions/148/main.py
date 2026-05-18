class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def sort_list(head: ListNode | None) -> ListNode | None:
    if not head:
        return head

    