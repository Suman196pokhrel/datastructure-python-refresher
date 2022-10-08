from tkinter.tix import Select


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

    def check_empty_dll(self,func):

        def wrapper_func():
           
                func()
        return wrapper_func

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
        if self.head is None:
            print("DLL is empty")
        else:
            if index <0 or index >= len(self):
                print(f"Index Out of Range ({0} - {len(self)})")
            else:
                if index == 0:
                    self.head = self.head.next
                elif index == len(self)-1:
                    itr = self.head
                    while itr.next.next:
                        itr = itr.next
                    itr.next = None
                    
                else:
                    itr = self.head
                    for _ in range(index-1):
                        itr = itr.next
                    itr.next.next.prev = itr
                    itr.next = itr.next.next
           
    def remove_front(self):
        if self.head is None:
            print("DLL is Empty")
        else:
            self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            print("DLL is Empty")
        elif len(self) == 1:
            self.head = None
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.prev.next = None
        


            


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.generate_dll_from_list([55])
    print(dll)
    dll.remove_last()
    print(dll)
