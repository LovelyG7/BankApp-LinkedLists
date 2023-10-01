class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

print(head.value)
print(head.next.value)
print(head.next.next.value)

""" 
Implementing a LinkedList

Since there is no linked list implementation in python, 
if we want a linked list we have to write one ourselves.
We can do this with an Object-Oriented approach. 
Where we consider each node in the list as an object with two attributes:
(value) and (next). 

We begin by making a node class. 

We set up a constructor method with the parameters of 'self' and 'value'
We will initialize the value of each node object with a value that will 
be passed in when the node is created. 

The next attribute will initialize in the constructor to 'None'
'None' is a special value in python that explicitly denotes 
the lack of any value.

What we have made here is a basic implementation of a linked list.
We can use this node class to instantiate a node object named 'head'.
This will be the first node in our linked list. 
We'll pass in a string of "1st Node".
And this will be the value for this node. 
And it will have a default next attribute of none
b/c we set that up in our constructor. 
That means it doesn't link to anything.

We say head.next which refers to the next attribute of 
the node that we just created.
Then we set it equal to a new node object that we instantiated
with a value of the string "2nd Node".
This both, creates a new node and saves a reference to this new
node's memory location of the next attribute of the head node.

This new "2nd Node" will have a next attribute initialized as 'None'.
This is now the tail node of our linked list. 

Notice we have a variable name that refers to the 1st Node in our linked list: head
However, we don't have a variable name for the second node.
The only reference we have to it is by using head.next.
So we can say head.next.next
Then set that equal to a reference of a new "3rd node"

What's happening here is head.next refers to the 2nd node
head.next.next refers to the next attribute of the second node
which now refers to the 3rd node
so now we have a 3rd node and this is the new tail node
We can keep going and adding more nodes to our link

Let's take a look at how we can access the values stored in ea. node
and we'll print them.

For the 1st node, we can access its value with head.value
If the 2nd node can be referenced with head.next, then it stands
to reason we should be able to access head.next.value
If the 3rd node can be referenced with head.next.next
then we can also access the 3rd node's value with head.next.next.value
"""