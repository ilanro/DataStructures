from LinkedList import *
from Stack import *
from Queue import *


def linked_test():

    my_list = LinkedList()
    for i in range(6):
        my_list.append(i)

    print(my_list)

    my_list.inverse()
    print(my_list)

    my_list = LinkedList()
    my_list.inverse()
    print(my_list)

    my_list.append(1)
    print(my_list)
    my_list.inverse()
    print(my_list)

def stack_test():
    my_stack = Stack()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print(my_stack)
    print(my_stack.top())
    print(my_stack)

    assert(len(my_stack)==3)

    print(my_stack.pop())
    print(my_stack)

    my_stack.pop()
    assert(my_stack.top() == my_stack.pop() == 1)
    print(my_stack)

def queue_test():
    my_queue = Queue()
    for i in range(6):
        my_queue.enqueue(i)

    print(my_queue)

    assert(my_queue.peek() == my_queue.dequeue())

if __name__ == "__main__":
    '''
    Testing data structues
    '''

    #linked_test()

    #stack_test()

    queue_test()
