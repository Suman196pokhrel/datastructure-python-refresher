def reverse(llist):
    itr = llist
    
    if llist is None:
        return llist
    else:
        # prev = None
        # curr = itr
        # nex = itr.next
        
        while itr.next is not None:
            temp = itr.next
            itr.prev, itr.next = itr.next,itr.prev
            itr = temp
        
        itr.prev, itr.next = itr.next,itr.prev
        llist = itr
    return llist