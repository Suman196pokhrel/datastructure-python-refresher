


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
    
    def __len__(self):
        if self.head is None:
            return 0
        else:
            itr = self.head
            count = 1
            while itr.next is not self.head:
                itr = itr.next
                count +=1
            return count

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
        if self.head is None:
            node = Node(data)
            node.next = self.head
            self.head = node
        else:
            itr = self.head
            while itr.next is not self.head:
                itr = itr.next
            node = Node(data)
            node.next = itr.next
            itr.next = node

    def insert_at(self,data,index):
        if index < 0 or index >=len(self):
            print(f"Index out of range ( 0 - {len(self)-1} )")
        elif self.head is None:
            print("CSLL is Empty")
        else:
            if index == 0:
                self.insert_at_start(data)
            else:
                node = Node(data)
                itr = self.head
                for _ in range(index-1):
                    itr = itr.next
                node.next = itr.next
                itr.next = node

    def remove_at_start(self):
        if self.head is None:
            print("CSLL is empty")
        else:
            itr = self.head
            while itr.next is not self.head:
                itr = itr.next
            itr.next = itr.next.next
            self.head = self.head.next

    def remove_at(self,index):
        if index <0 or index >=len(self):
            print(f"Index out of Range ( 0 - {len(self)-1})")
        elif self.head is None:
            print("CSLL is empty")
        else:
            if index == 0:
                self.remove_at_start()
            else:
                itr = self.head
                for _ in range(index-1):
                    itr = itr.next
                itr.next = itr.next.next
    
    def generate_csll(self,data):
        self.head = None
        for elem in data[::-1]:
            self.insert_at_start(elem)

    def update_value(self,index,new_data):
        if index <0 or index >= len(self):
            print(f"Index out of range( 0 - {len(self)-1})")
        elif self.head is None:
            print("SLL is empty")
        else:
            itr  = self.head
            for _ in range(index):
                itr = itr.next
            itr.data = new_data


if __name__=="__main__":
    csll = CircularLinkedList()
    csll.generate_csll(data=[11,22,33,44,55])
    print(csll)
    csll.update_value(index=4,new_data=3333)
    print(csll)
