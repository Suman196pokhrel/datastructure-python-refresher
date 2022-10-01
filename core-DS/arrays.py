import os
import time
from colorama import Fore


# GLOABL VARS
# DEFAULT VALUE
user_array = [11, 22 , 33, 44, 55]

def create_Array():
    os.system("cls")
    global user_array
    print(Fore.YELLOW+"""
    --------------CREATE AN ARRAY------------------
    
    Choose any of the following options
    1. Enter  elements for your array as Example: 1_2_3_4_5 
    2. Exit
    """)
    inp = int(input())

    if inp == 1:
        try:
            print(f"Enter  elements for your array as Example: 1_2_3_4_5 ")
            user_array = list( map(int,input("\x1B[31m ").split()))
            print("Array created => ",user_array)
            return user_array
        except Exception as e:
            print("Invalid data type, only int supported")
    else:
        return None


def insert_element():
    os.system("cls")
    global user_array
    print(Fore.YELLOW+"""
    --------------INSERTING AN ELEMENT IN ARRAY------------------
    
    Choose any of the following options
    1. Insertr at beginning
    2. Insert at middle
    3. Insert at last
    4. Exit
    """)
    inp = int(input())
    if inp<=3 and inp >=1:
        if inp==1:
            elem = int(input("Provide an element to insert : "))
            user_array.insert(0,elem)
        elif inp==2:
            elem = (input("Provide  index_element) Example: 3 22 :  ").split())
            user_array.insert(int(elem[0]), int(elem[-1]))
        elif inp==3:
            elem = int(input("Provide an element to insert : "))
            user_array.append(elem)
        else:
            return None


def delete_element():
    os.system("cls")
    global user_array
    print(Fore.YELLOW+"""
    --------------Deleting AN ELEMENT IN ARRAY------------------
    
    Choose any of the following options
    1. Delete at beginning
    2. Delete at middle
    3. Delete at last
    4. Exit
    """)
    inp = int(input())
    if inp<=3 and inp >=1:
        if inp==1:
            user_array.pop(0)
        elif inp==2:
            index = int(input(f"Provide  index) index range : 0 - {len(user_array)} :  "))
            if index in range(0,len(user_array)):
                user_array.pop(index)
            else:
                print("Invalid Index")
        elif inp==3:
            user_array.pop()
        else:
            return None

def search_first_index():
    os.system("cls")
    global user_array
    print(Fore.YELLOW+"""
    --------------SEARCH INDEX OF FIRST ELEMENT IN ARRAY------------------
    
    Choose any of the following options
    1. Enter the Element to search for
    2. Exit

    """)
    inp = int(input())
    if inp<=2 and inp >=1:
        if inp==1:
            val = int(input(f"Enter the element to search for {user_array}: \n "))
            ind = user_array.index(val)
            print(f"The index of first appearance of {val} is {ind}")
            time.sleep(5)
        
        else:
            return None


if __name__ == "__main__":
    while True:
        os.system("cls")
        print(Fore.CYAN+f"""
        _____________________________________________
        ----------Array Operation Station------------ 
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """,end="")
        print(Fore.BLUE+ f"""
        {user_array}
        """)

        print(Fore.GREEN +"""

        Choose any of the following Operations

        1. Create New Array                                      
        2. Insert Element
        3. Delete Element
        4. Search index of elem
        5. Sort Array
        6. Merge Arrays
        7. Exit

        """)
        user_inp = input()

        if(user_inp=="1"):
            create_Array()
        elif user_inp =="2":
            insert_element()
        elif user_inp =="3":
            delete_element()
        elif user_inp =="4":
            search_first_index()
        elif user_inp =="5":
            pass
        elif user_inp =="6":
            pass
        else:
            print("Shutting Down Program")
            break
