class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack using Linked List
class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            last = self.head
            self.head = last.next
            last.next = None

    def peek(self):
        if self.is_empty():
            return None
        temp = self.head
        print(temp.data)

    def printStack(self):
        li = []
        temp = self.head
        while temp:
            li.append(temp.data)
            temp = temp.next
        print(li)

