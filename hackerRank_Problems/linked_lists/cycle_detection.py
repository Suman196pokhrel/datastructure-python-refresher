def has_cycle(head):

    if (head == None):
        return 0
    else:
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return 0
            else:
                slow = slow.next;
                fast = fast.next.next;
        return 1

    # Method 2
        
    # visited = set()
    # f = head
    # while f:
    #     i = id(f)
    #     if i in visited:
    #         return 1
    #     visited.add(i)
    #     f = f.next
    # return 0
    