from linked_list import *


class OrdLinkedList(LinkedList):

    def insert(self, data):
        if self.is_empty():
            super().insert(data)
        else:
            prev = None
            current = self.head
            while data <= current.get_priority() and current != None:
                prev = current
                current = current.get_next
            temp = Node(data)
            temp.set_next(current)
            prev.set_next(temp)
            self.size += 1

    def extractMax(self):
        if self.is_empty():
            return
        temp = self.head
        self.head = temp.get_next()
        self.size -= 1
        return temp
