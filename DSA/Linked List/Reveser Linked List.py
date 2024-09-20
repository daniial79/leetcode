def reverse_list(head):
    
    if head is None or head.Next is None:
        return head
    
    current = head
    before = None
    after = None
    
    while current is not None:
        after = current.next
        current.next = before
        before = current
        current = after
    
    # returning before pointer as head of reversed linked list
    return before