import os


# GLOABL VARS
user_array = []

def create_Array():
    global user_array
    print("""
    --------------CREATE AN ARRAY------------------
    
    Choose any of the following options
    1. Enter the length of array
    2. Exit
    """)
    inp = input()

    if inp == "1":
        try:
            print(f"Enter  elements for your array as Example: 1_2_3_4_5 ")
            user_array =list( map(int,input().split()))
            print("Array created => ",user_array)
            return user_array
        except Exception as e:
            print("Invalid data type, only int supported")
    else:
        return None


    





if __name__ == "__main__":
    while True:
        os.system("cls")
        print(f"""
        _____________________________________________
        ----------Array Operation Station------------ 
        {user_array}

        Choose any of the following Operations

        1. Create New Array                                      
        2. Traverse
        3. Insert Element
        4. Delete Element
        5. Search index of elem
        6. Sort Array
        7. Merge Arrays
        8. Exit

        """)
        user_inp = input()

        if(user_inp=="1"):
            create_Array()
        elif user_inp =="2":
            pass
        elif user_inp =="3":
            pass
        elif user_inp =="4":
            pass
        elif user_inp =="5":
            pass
        elif user_inp =="6":
            pass
        elif user_inp =="7":
            pass
        else:
            print("Shutting Down Program")
            break
