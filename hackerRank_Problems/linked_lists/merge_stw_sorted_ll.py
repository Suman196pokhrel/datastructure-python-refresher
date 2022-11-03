def mergeLists(head1, head2):
    head3 = SinglyLinkedListNode(-1)
    node = head3
    
    while head1 and head2:
        if head1.data <= head2.data:
            node.next = head1
            head1 = head1.next
        else:
            node.next = head2
            head2 = head2.next
        node = node.next
    
    if head1:
        node.next = head1
    if head2:
        node.next = head2
    
    return head3.next