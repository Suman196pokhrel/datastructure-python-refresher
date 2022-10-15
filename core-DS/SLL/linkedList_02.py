

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
            list_str = "self.head"
            while itr:
                
                list_str  = list_str + " --> " +f"[ {str(itr.data)} ]" 
                itr = itr.next
            return list_str

    def deep_print(self):
        if self.head is None:
            return "Linked List is Empty"
        else:
            itr = self.head
            list_str = "self.head"
            while itr:
                
                list_str  = list_str + " --> " +f"[{str(itr.data)} - {hex(id(itr))} | {hex(id(itr.next))}]" 
                itr = itr.next
            print(list_str)

    def box_print(self):
        if self.head is None:
            return "Linked List is Empty"
        else:
            itr = self.head
            num = len(self)
            for _ in range(num):
                print("-"*23,end=f"{' '*3}      ")
            print("")
            # print("Head ==> ", end="")
            while itr:
                print(f"|{str(itr.data).center(5)}|{str(hex(id(itr.next))).center(15)}|",end=f"{' '*3}==>   ")
                itr = itr.next
            
            print("None")
            for _ in range(num):
                print("-"*23,end=f"{' '*3}      ")
            print("")
            for i in range(num):
                print("|",f"val".center(5),f"|  Next       |".center(15),end=f"{' '*3}      ")
                
            print("")
            for _ in range(num):
                print("-"*23,end=f"{' '*3}      ")
           
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

    def search_by_value(self,value):
        if self.head is None:
            print("Linked list is empty ")
        else:
            itr = self.head
            count = 0
            while itr:
                if itr.data == value:
                    print(f"{value} found at index {count}")
                    break
                count +=1
                itr = itr.next
            if count == len(self):
                print("Your value is not present in the linked list")

    def remove_by_Value(self,value):
        if self.head is None:
            print("Linkedlist is empty")
        
        elif self.head.data == value:
            self.head = self.head.next

        
        else:
            itr_1 = self.head
            while  itr_1.next.data != value:
                itr_1 = itr_1.next
            rem_node = itr_1.next
            itr_1.next = itr_1.next.next
            rem_node.next = None

    def reverse_llist(self,type_1=None):
        if self.head is None:
            print("Linked List is empty")
        else:
            curr = self.head
            nex = self.head.next
            prev = None
            while nex:
                curr.next = prev
                prev = curr
                curr = nex
                nex = nex.next
            curr.next = prev
            self.head = curr
        


                
  

if __name__ == "__main__":
    llist = LinkedList()

    llist.generate_llist_from_list([11,22,33,44,55])
    print(llist)
    llist.reverse_llist()
    print(llist)
    llist.search_by_value(55)


