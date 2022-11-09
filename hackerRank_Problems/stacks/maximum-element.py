def getMax(operations):
    myStack = []
    max_arr = []
    max_val = 0
    
    for operation in operations:
        
        if operation[0]=="1":
            elem = int(operation[1:])
            myStack.append(elem)
            
            if elem > max_val:
                max_val = elem
                
        elif operation[0] == '2':
            myStack.pop()
            max_val = max(myStack) if len(myStack) else 0
            
        else:
            max_arr.append(max_val) 
        

    
    return max_arr