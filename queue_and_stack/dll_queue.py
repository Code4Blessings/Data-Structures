import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()
    def enqueue(self, value):
        self.size +=1
        #Definition of enqueue is should add an item to the back of the queue.
        #Therefore we can use add_to_tail function?
        self.storage.add_to_tail(value)

    def dequeue(self):
        #Definition of dequeue is it should remove and return an item from the front of the queue.
        #Therefore use remove_from_head function
        return self.storage.remove_from_head()
    def len(self):
        return self.size
