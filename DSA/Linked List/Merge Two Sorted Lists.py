class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        dummy = ListNode()
        tail = dummy

        ptr1, ptr2 = list1, list2

        while ptr1 is not None and ptr2 is not None:
            
            if ptr1.val <= ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next
            
            tail = tail.next
        
        if ptr1 is None:
            tail.next = ptr2
        else:
            tail.next = ptr1
        
        return dummy.next