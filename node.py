class Node:
    def __init__(self, data):
        self.priority = data
        self.next = None

    def get_priority(self):
        return self.priority

    def get_next(self):
        return self.next

    def set_priority(self, new_data):
        self.priority = new_data

    def set_next(self, new_next):
        self.next = new_next
