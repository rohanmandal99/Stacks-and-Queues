class Stack:
    def __init__(self):
        self.li = []

    def is_empty(self):
        if not self.li:
            return True
        else:
            return False

    def push(self, new_data):
        self.li.append(new_data)

    def pop(self):
        self.li.pop()

    def peek(self):
        print(self.li[len(self.li) - 1])

    def print(self):
        rev = []
        for i in self.li:
            rev.append(i)
        print(rev)

