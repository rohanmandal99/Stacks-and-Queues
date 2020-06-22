class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def dequeue(self):
        if self.head is None:
            return
        self.head = self.head.next

    def printQueue(self):
        li = []
        temp = self.head
        while temp is not None:
            li.append(temp.data)
            temp = temp.next
        print(li)

    def peek(self):
        print(self.head.data)

