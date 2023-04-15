"""Linked List implementation of the PriorityQueueInterface."""
from __future__ import annotations

from dataclasses import dataclass, field

from node import Node
from priority_queue_interface import PriorityQueueInterface


@dataclass
class LinkedList(PriorityQueueInterface):
    """Linked List implementation of the PriorityQueueInterface."""

    size: int = field(init=False, default=0)
    """Size of the priority queue."""
    head: Node | None = field(init=False, default=None)
    """Head of the linked list."""

    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None

    def insert(self, data: float | int) -> None:
        """Insert an element in the priority queue.

        Insert always at the head.
        Complexity O(1).
        """
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp
        self.size += 1

    def extractMax(self) -> float | int | None:
        """Extract the maximum element from the priority queue.

        Complexity O(n).
        Returns None if the list is empty.
        """
        if self.head is None:
            return None
        else:
            prev = self.head
            max_priority_node = prev
            prev_max_priority = None
            current = prev.get_next()
            while current is not None:
                if max_priority_node.priority < current.priority:
                    max_priority_node = current
                    prev_max_priority = prev
                prev = current
                current = current.get_next()
            if prev_max_priority is None:
                self.head = max_priority_node.get_next()
            else:
                prev_max_priority.set_next(max_priority_node.get_next())
        self.size -= 1
        return max_priority_node.priority

    def remove(self, data: float | int) -> None:
        """Remove an element from the priority queue.

        Complexity O(n).
        """
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.get_priority() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        self.size -= 1

    def search(self, data: float | int) -> bool:
        """Search an element in the priority queue. Return True if found."""
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_priority() == data:
                found = True
            else:
                current = current.get_next()
        return found
