import os
import time
from colorama import Fore


# GLOABL VARS
user_array = [11, 22 , 33, 44, 55]

def create_Array():
    global user_array
    print(Fore.YELLOW+"""
    --------------CREATE AN ARRAY------------------
    
    Choose any of the following options
    1. Enter the length of array
    2. Exit
    """)
    inp = input()

    if inp == "1":
        try:
            print(f"Enter  elements for your array as Example: 1_2_3_4_5 ")
            user_array =list( map(int,input("\x1B[31m "+"").split()))
            print("Array created => ",user_array)
            return user_array
        except Exception as e:
            print("Invalid data type, only int supported")
    else:
        return None


def insert_element():
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
            pass
        elif user_inp =="4":
            pass
        elif user_inp =="5":
            pass
        elif user_inp =="6":
            pass
        else:
            print("Shutting Down Program")
            break
