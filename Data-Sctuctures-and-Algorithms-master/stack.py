# SIMPLE STACK IMPLEMENTATION

class Stack():
    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "STACK IS EMPTY"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "STACK IS EMPTY"
    
    def get_stack(self):
        return self.items
