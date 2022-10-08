class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "DLL is Empty"
        else:
            itr = self.head
            dllist = "self.head "
            while itr:
                dllist = dllist + " ---> " + str(itr.data)
                itr = itr.next
                
            return dllist

    def __len__(self):
        if self.head is None:
            return 0
        else:
            itr = self.head
            count = 1
            while itr.next:
                count +=1
                itr = itr.next
            return count

    def insert_at_start(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insert_at_end(self,data):
            if self.head is None:
                node = Node(data)
                self.head = node
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next

                node = Node(data)
                itr.next = node
                node.prev = itr
                
    def insert_at(self,data,index):
        if index >=len(self) or index <0:
            print("Index Out of Range")
        else:
            if index == 0 :
                self.insert_at_start(data)
            else:
                itr = self.head
                for _ in range(index-1):
                    itr = itr.next
                node = Node(data,next=itr.next,prev=itr)
                itr.next.prev = node
                itr.next = node
        
    def generate_dll_from_list(self,user_list):
        self.head = None
        for data in user_list:
            self.insert_at_end(data)

    def remove_at(self,index):
        pass

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.generate_dll_from_list([11,22,33,44,55])
    print(dll)
    dll.insert_at(data=23,index=0)
    dll.remove_at(0)
    print(dll)
