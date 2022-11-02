def reverse(llist):
    prev = None
    curr = llist
    nex = curr.next
    while nex is not None:
        curr.next = prev
        prev = curr
        curr = nex
        nex = nex.next
    curr.next = prev
    llist = curr
    
    return llist