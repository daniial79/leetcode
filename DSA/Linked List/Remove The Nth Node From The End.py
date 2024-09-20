def remove_nth_from_end(head):
    if head is None or head.next is None:
        return None

    scout, prev = head, head

    for _ in range(n):
        scout = scout.next

    if scout is None:
        return head.next
    
    while scout.next is not None:
        scout = scout.next
        prev = prev.next

    prev.next = prev.next.next

    return head        