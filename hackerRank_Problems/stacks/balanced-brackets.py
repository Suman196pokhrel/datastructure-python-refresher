from collections import deque

a = '[{()}]'


def isBalanced(s):
    check = {")":"(" , "]":"[" , "}":"{" }
    myStack = []
    for elem in s:
        # if elem in opening brackets
        if elem in check.values():
            myStack.append(elem)
            
        # if elem is closing bracket 
        elif myStack and check[elem] == myStack[-1]:
            myStack.pop()
        else:
            return 'NO'
            
    if myStack == []:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        print(isBalanced(s))

        

   
