from LinkedList import *

if __name__ == "__main__":
    '''
    Testing data structues
    '''

    # Linked List:

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

