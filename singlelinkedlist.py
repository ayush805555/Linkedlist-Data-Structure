class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next is not None


class Linkedlist:
    def __init__(self):
        self.head = None

    def listLength(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        print(count)

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, "-- >", end="")
            current = current.next

    def r_traverse(self):
        prev = None
        current = self.head
        while current is not None:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        self.head = prev

    def insertAtBegining(self, data):
        newnode = Node(data)
        newnode.setData(data)
        if self.head == 0:
            self.head = newnode
        else:

            newnode.setNext(self.head)
            self.head = newnode

    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newnode

    def insertAtMiddle(self, pos, data):
        current = self.head
        if pos < 1:
            print("Invalid position!")
        if pos == 1:
            self.insertAtBegining(data)
        else:
            while pos != 0:
                pos = pos - 1
                if pos == 1:
                    newnode = Node(data)
                    newnode.next = current.next
                    current.next = newnode
                    break
                current = current.next
                if current is None:
                    break
            if pos != 1:
                print("position out of range")
        return self.head

    def deleteAtBegining(self):
        if not self.head:
            return None
        else:
            self.head = self.head.getNext()

    def deleteAtEnd(self):
        if not self.head:
            return None
        else:
            current = self.head
            prev = self.head

            while current.getNext() is not None:
                prev = current
                current = current.getNext()
            prev.setNext(None)

    def deleteAtMiddle(self, pos):
        count = 0
        current = self.head
        prev = self.head
        if self.head is None:
            return None
        else:
            while current.getNext() is not None or count < pos:
                count = count + 1
                if count == pos:
                    prev.next = current.next
                    return
                else:
                    prev = current
                    current = current.getNext()

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


llist = Linkedlist()
llist.insertAtEnd(1)
llist.insertAtEnd(2)
llist.insertAtEnd(3)
llist.insertAtEnd(4)
llist.insertAtEnd(5)
llist.insertAtEnd(6)
print(" \nInserted at End List is:\n")
llist.traverse()
print("\nInserted at Begining List is\n")
llist.insertAtBegining(7)
llist.insertAtBegining(8)
llist.insertAtBegining(9)
llist.insertAtBegining(10)
llist.traverse()
print("\nNow Insert At Pos:-->2 with data --> 11\n")
llist.insertAtMiddle(2, 11)
llist.traverse()
print("\n Delete First Node of List\n")
llist.deleteAtBegining()
llist.traverse()
print("\nDelete Last Node of List\n")
llist.deleteAtEnd()
llist.traverse()
print("\n Delete At Pos --> 2\n")
llist.deleteAtMiddle(2)
llist.traverse()
print("\n Length of Linkedlist Is : \n")
llist.listLength()
print("\nReverse of List\n")
llist.r_traverse()
llist.traverse()
print("\nMaximum among the above List is:\n")
llist.maximumofList()
print("\nMinimum among the above List is:\n")
llist.minimumofList()
print("\nNow Original List after all operation performed\n")
llist.traverse()
