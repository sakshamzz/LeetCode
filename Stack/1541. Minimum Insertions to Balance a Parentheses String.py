def minInsertions(str):
    myStack = []
    for i in str:
        if myStack[-1] != i:
            myStack.pop(i)
        else:
            myStack.append(i)     
    print(myStack)
minInsertions("(()))")
