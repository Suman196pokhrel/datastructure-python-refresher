def removeDuplicates(llist):
    if llist is None:
        return llist
    else:
        curr = llist
        nex = llist.next
        while curr.next:
            if curr.data != nex.data:
                nex = nex.next
                curr = curr.next
            else:
                nex = nex.next
                curr.next = curr.next.next
        return llist
                