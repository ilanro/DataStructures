from LinkedList import *


class Stack:
    def __init__(self):
        self.items = LinkedList()

    def __len__(self):
        return len(self.items)

    def push(self, new_val):
        self.items.insert(0, new_val)

    def pop(self):
        if len(self) == 0:
            return
        item = self.items.head.val
        self.items.remove_at(0)
        return item

    def top(self):
        return self.items.head.val

    def __str__(self):
        if len(self) == 0:
            return "Empty Stack"
        return str(self.items)