from LinkedList import *

class Queue:
    def __init__(self):
        self.items = LinkedList()

    def __len__(self):
        return len(self.items)

    def enqueue(self, new_val):
        self.items.append(new_val)

    def dequeue(self):
        if len(self.items) == 0:
            return
        item = self.items.head.val
        self.items.remove_at(0)
        return item

    def peek(self):
        if self.is_empty():
            return
        return self.items.head.val

    def is_empty(self):
        return len(self.items) <= 0

    def __str__(self):
        if len(self) == 0:
            return "Empty Queue"
        return str(self.items)