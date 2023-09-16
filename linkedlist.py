
class node:
    int data
    node next
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist:
    int size
    node head = null
    def traverse(self, head):
        temp = head
        if(temp is Not None):
            while(temp.next is None):
                print(temp.data)
                temp = temp.next
                size++


# Traverse linked list

# Insert into linked list

# Delete from Linked List
