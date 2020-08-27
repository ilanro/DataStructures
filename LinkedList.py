class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __len__(self):
        return self.count

    def append(self, new_val):
        self.insert(self.count, new_val)

    def insert(self, index: int, new_val):

        new_node = Node(val = new_val)
        if index > self.count:
            index = self.count
        if index < 0:
            index = 0
        count = 0
        prev = it = self.head
        while count != index:
            prev = it
            count = count + 1
            it = it.next
            if it is None:
                break
        self.count = self.count + 1
        if it == self.head:
            new_node.next = self.head
            self.head = new_node
            return
        new_node.next = it.next if it is not None else None
        prev.next = new_node

    def remove_at(self, index: int):
        if index >= self.count:
            return
        count = 0
        prev = it = self.head
        while count != index:
            prev = it
            count = count + 1
            it = it.next
        self.count = self.count - 1
        if it == self.head:
            self.head = self.head.next
        prev.next = it.next


    def remove_value(self, all_instances=False):
        pass

    def inverse(self):
        if self.count == 0:
            return
        helper = self.head
        next_node = helper.next
        helper.next = None
        while next_node is not None:
            prev = helper
            helper = next_node
            next_node = helper.next
            helper.next = prev
        self.head = helper

    def __str__(self):
        if self.count == 0:
            return "Empty List"
        res=str(self.head.val)
        it = self.head.next
        while it is not None:
            res = res + "->" + str(it.val)
            it = it.next
        return res