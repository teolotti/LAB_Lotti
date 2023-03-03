from node import*

class LinkedList:
    size = 0
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert(self, data):
        temp = Node(data);
        temp.set_next(self.head)
        self.head = temp

    def extractMax(self):
        if self.is_empty():
            return
        else:
            prev = self.head
            current = prev.get_next()
            temp = prev
            prev_t = None
            while current != None:
                if temp.get_data < current.get_data:
                    temp = current
                    prev_t = prev
                prev = current
                current = current.get_next()
            if prev_t == None:
                self.head = temp.get_next()
            else:
                prev_t.set_next(temp.get_next())









