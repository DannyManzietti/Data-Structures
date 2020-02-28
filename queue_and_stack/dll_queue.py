from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_top(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        item = self.storage.remove_from_bottom()
        self.size -= 1
        return item

    def len(self):
        return self.size
