class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    
    if head is None or head.next is None:
        return False

    tortoise, hare = head, head

    while hare.next is not None and hare.next.next is not None:
        hare = hare.next.next
        tortoise = tortoise.next

        if hare is tortoise:
            return True
    
    return False