from LinkedList import *


class Stack:
    def __init__(self):
        self.items = LinkedList()

    def __len__(self):
        return len(self.items)

    def push(self, new_val):
        self.items.insert(0, new_val)

    def pop(self):
        item = self.items.head
        self.items.remove_at(0)
        return item

    def top(self):
        return self.items.head
