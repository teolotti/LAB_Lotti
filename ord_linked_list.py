"""Ordered Linked List implementation."""
from dataclasses import dataclass

from linked_list import LinkedList
from node import Node


@dataclass
class OrdLinkedList(LinkedList):
    """Ordered Linked List implementation."""

    def insert(self, data: float | int) -> None:
        """Insert an element in the priority queue.

        Insert in order.
        Complexity O(n).
        """
        if self.is_empty():
            super().insert(data)
        else:
            prev = None
            current = self.head
            while current is not None and data <= current.get_priority():
                prev = current
                current = current.get_next()
            if prev is None:
                super().insert(data)
            else:
                temp = Node(data)
                temp.set_next(current)
                prev.set_next(temp)
                self.size += 1

    def extractMax(self) -> float | int | None:
        """Extract the maximum element from the priority queue.

        Complexity O(1).
        Returns None if the list is empty.
        """
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = temp.get_next()
            self.size -= 1
            return temp.priority
