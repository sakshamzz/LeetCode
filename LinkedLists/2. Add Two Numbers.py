class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next          


if __name__ == '__main__':
    sList = LinkedList()
    sList.head = Node(4)
    sList1 = Node(6)
    sList2 = Node(12)

    sList.next = sList1
    sList1.next = sList2

    sList.printList()

