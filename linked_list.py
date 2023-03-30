from node import *

from priority_queue_interface import *


class LinkedList(PriorityQueueInterface):
    def __init__(self):
        self.size = 0
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp
        self.size += 1

    def extractMax(self):
        if self.is_empty():
            return
        else:
            prev = self.head
            current = prev.get_next()
            temp = prev
            prev_t = None
            while current != None:
                if temp.get_priority() < current.get_priority():
                    temp = current
                    prev_t = prev
                prev = current
                current = current.get_next()
            if prev_t == None:
                self.head = temp.get_next()
            else:
                prev_t.set_next(temp.get_next())
        self.size -= 1
        return temp

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.get_priority() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        self.size -= 1

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_priority() == item:
                found = True
            else:
                current = current.get_next()
        return found
