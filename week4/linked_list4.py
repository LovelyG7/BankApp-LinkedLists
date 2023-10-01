"""Doublenode is an atomic structure.
Its key characteristics the attributes we build into it can hold some data of value. 
and it can hold a link to the next node. 
For the doubly linked list it can hold a link to the previous node. 
We don't know what these links are going to be yet, so we initialize them as None.
"""

class Doublenode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
"""Now that we have the atomic structure we can define the doubly linked list class. 
This classes constructor will contain two attributes:head and tail.
Which means when a doubly linked list object is first instantiated it will not contain any nodes. 
"""

class DoublyLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Doublenode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)

dlist = DoublyLinkedLists()
dlist.append("First Node")



