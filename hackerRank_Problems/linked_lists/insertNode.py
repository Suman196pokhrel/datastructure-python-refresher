def insertNodeAtPosition(llist, data, position):
    # Write your code here
    itr = llist
    node = SinglyLinkedListNode(data)
    if llist is None:
        llist = node
        return llist
    else:
        for _ in range(position -1):
            itr = itr.next
        node.next = itr.next
        itr.next = node
        return llist