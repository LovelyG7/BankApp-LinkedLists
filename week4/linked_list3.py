class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
There's one bit of information that a linked list must know
about itself

linked lists must always know where its head is; 
so set up constructor method init with only the parameter of self. 
Each instantiation will point to itself so there is a place holder for objects that don't exist yet; 
which means we can make useful statements about it. """

class LinkedList: 
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

#At this point new node not attached to anything and doesn't refer to any memory address or vice versa.  
#We need to find the tail node of the list. Then we can link this new node to it. 
# But we need to be able to append to a list that doesn't have any nodes yet also. 
        if self.head is None: 
            self.head = new_node
            print("Head Node created: ", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next
        
        node.next = new_node
        print("Appended new Node with value:", node.next.value)

llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")


"""
Linked List Class

When implementing a linked list in python by 
using classes and objects
it's common practice to create a separate class
for the linked list itself
which will us the node class.
This lets us use commonly used methods directly on 
the linked list class. 
"""