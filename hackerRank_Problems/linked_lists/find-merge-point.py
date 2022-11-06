def findMergeNode(head1, head2):
    itr1 = head1
    itr2 = head2
    
    while itr1:
        itr1.data  = str(itr1.data) + "s"
        itr1 = itr1.next
    while itr2:
        if str(itr2.data)[-1] == "s":
            return int(itr2.data[:-1])
        itr2 = itr2.next