import os

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Linked List is Empty"
        else:
            itr = self.head
            list_str = ""
            while itr:
                
                list_str  = list_str + " --> " + str(itr.data) 
                itr = itr.next
            return list_str


    def __len__(self):
        if self.head is None:
            return 0
        else:
            itr  = self.head
            count = 0
            while itr:
                count +=1
                itr = itr.next
            return count


    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):

        if self.head is None:
            self.insert_at_begining(data)
        else:
            node = Node(data,None)
            itr = self.head

            while itr.next:
                itr = itr.next
            
            itr.next = node

    def insert_at(self,data,index):
        if index < 0 and index > len(self):
            print("Invalid Index")
        else:
            if index == 0:
                self.insert_at_begining(data)
            else:
                itr = self.head
                for _ in range(index-1):
                    itr = itr.next
                node = Node(data,itr.next)
                itr.next = node


    def generate_llist_from_list(self,user_list):
        self.head = None
        for data in user_list:
            self.insert_at_end(data)

    def remove_at(self,index):
        
        if index <0 or  index > len(self):
            print(f"Index Out of Range: (0 - {len(self)-1})")
        
        elif index >=0 and index <= len(self):
            if index == 0:
                self.head = self.head.next
            else:
                itr = self.head
                for _ in range(index-1):
                    itr = itr.next
                itr.next = itr.next.next



  

if __name__ == "__main__":
    llist = LinkedList()

    llist.generate_llist_from_list(["Login Page","Dashboard Page","Profile Page","Personel Info page"])
    print(llist)
    llist.insert_at("Test1",0)
    print(llist)
    llist.insert_at("Test1",len(llist))
    print(llist)

    llist.insert_at("Test1",2)

    print(llist)

