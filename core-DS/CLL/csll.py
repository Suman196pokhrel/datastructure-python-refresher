from select import select
from tkinter.messagebox import NO


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None


    def __str__(self):
        if self.head is None:
            return "Circular Linked List is Empty"
        else:
            itr = self.head
            csll = "self.head ==> "
            while itr:
                csll = csll +" ---> " +str(itr.data)
                itr = itr.next
                if itr is self.head:
                    break
            return csll


    
    def insert_at_start(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
            node.next = self.head
        else:
            itr = self.head
            node = Node(data)
            while itr.next is not self.head:
                itr= itr.next


            node.next = self.head   
            self.head = node
            itr.next = self.head
             
    def insert_at_end(self,data):
        pass

    def insert_at_mid(self,data):
        pass


if __name__=="__main__":
    csll = CircularLinkedList()
    csll.insert_at_start(55)
    csll.insert_at_start(44)
    csll.insert_at_start(33)
    csll.insert_at_start(22)
    csll.insert_at_start(11)

    print(csll)
