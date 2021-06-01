class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def hasNext(self):
        return self.next is not None

    def hasPrev(self):
        return self.prev is not None


class DoublyLinkedlist:

    def __init__(self):
        self.head = None
        self.tail = self.head

    def listLength(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        print(count)

    def traversing(self):
        if self.head is None:
            return None
        else:
            current = self.head
            while current is not None:
                print(current.data, "-- >", end="")
                current = current.getNext()

    def r_traversing(self):
        prev = None
        current = self.head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev
        return self.head

    def insertAtBegining(self, data):

        newnode = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = newnode
        else:
            newnode.setPrev(None)
            newnode.setNext(self.head)
            self.head.setPrev(newnode)
            self.head = newnode

    def insertAtEnd(self, data):

        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(Node(data, None, current))
            self.tail = current.getNext()

    def getNode(self, pos):
        current = self.head
        if current is None:
            return None
        count = 0
        while count < pos and current.getNext() is not None:
            current = current.getNext()
            if current is None:
                break
            count = count + 1
        return current

    def insertAtMiddle(self, pos, data):
        newnode = Node(data)
        if self.head is None or pos == 0:
            self.insertAtBegining(data)
        else:
            while pos != 0:
                pos = pos - 1
                if pos == 1:
                    temp = self.getNode(pos)
                    if temp is None or temp.getNext() is None:
                        self.insertAtEnd(data)
                    else:
                        newnode.setNext(temp.getNext())
                        newnode.setPrev(temp)
                        temp.getNext().setPrev(newnode)
                        temp.setNext(newnode)

    def deleteAtBegining(self):
        if self.head is not None:
            self.head = self.head.getNext()
            if self.head is not None:
                self.head.prev = None

    def deleteAtEnd(self):
        if self.head is None:
            return None
        else:
            if self.head is not self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = self.tail = None

    def deleteAtMiddle(self, pos):
        if pos < 1:
            return None

        elif pos == 1 and self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
        else:

            temp = self.head
            for i in range(1, pos - 1):
                if temp is not None:
                    temp = temp.next

            if temp is not None and temp.next is not None:
                temp.next = temp.next.next
                if temp.next.next is not None:
                    temp.next.next.prev = temp.next
            else:
                return None

    def maximumofList(self):
        current = self.head
        largest = current.getData()
        while current is not None:
            if largest < current.getData():
                largest = current.getData()
            current = current.getNext()
        print(largest)

    def minimumofList(self):
        current = self.head
        smallest = current.getData()
        while current is not None:
            if smallest > current.getData():
                smallest = current.getData()
            current = current.getNext()
        print(smallest)


llist = DoublyLinkedlist()

llist.insertAtEnd(1)
llist.insertAtEnd(2)
llist.insertAtEnd(3)
llist.insertAtEnd(4)
llist.insertAtEnd(5)
llist.insertAtEnd(6)
print(" \nInserted at End List is:-\n")
llist.traversing()
print("\nInserted at Begining of the List is:-\n")
llist.insertAtBegining(7)
llist.insertAtBegining(8)
llist.insertAtBegining(9)
llist.insertAtBegining(10)
llist.traversing()
print("\nNow Insert At Pos:-->2 with data --> 99\n")
llist.insertAtMiddle(2, 99)
llist.traversing()
print("\n Delete First Node of List\n")
llist.deleteAtBegining()
llist.traversing()
print("\nDelete Last Node of List\n")
llist.deleteAtEnd()
llist.traversing()
print("\n Delete At Pos --> 2\n")
llist.deleteAtMiddle(2)
llist.traversing()
print("\n Length of Linkedlist Is : \n")
llist.listLength()
print("\nReverse of List\n")
llist.r_traversing()
llist.traversing()
print("\nMaximum among the above List is:\n")
llist.maximumofList()
print("\nMinimum among the above List is:\n")
llist.minimumofList()
print("\nNow Original List after all operation performed\n")
llist.traversing()