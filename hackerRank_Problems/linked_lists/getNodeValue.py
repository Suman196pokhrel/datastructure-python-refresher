def getNode(llist, positionFromTail):
    itr = llist
    count = 0
    while itr.next is not None:
        count +=1
        itr = itr.next
    
    for _ in range(count-positionFromTail):
        llist = llist.next
    return llist.data