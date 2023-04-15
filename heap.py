"""Implementation of a heap data structure."""
from __future__ import annotations

from dataclasses import dataclass, field

from priority_queue_interface import PriorityQueueInterface


@dataclass
class Heap(PriorityQueueInterface):
    """Implementation of a heap data structure."""

    size: int = field(init=False, default=0)
    """Size of the heap."""
    queue: list[float | int] = field(init=False, default_factory=list)
    """Heap data structure."""

    def parent(self, i: int) -> int:
        """Get the parent index of a node."""
        return (i - 1) // 2

    def left(self, i) -> int:
        """Get the left child index of a node."""
        return 2 * i + 1

    def right(self, i) -> int:
        """Get the right child index of a node."""
        return 2 * i + 2

    def swap(self, a: int, b: int) -> None:
        """Swap two elements in the heap given their indexes."""
        self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

    def maxHeapify(self, ind: int) -> None:
        """Max heapify a node given its index.

        Complexity O(log n).
        """
        left = self.left(ind)
        right = self.right(ind)
        if left < self.size and self.queue[left] > self.queue[ind]:
            largest = left
        else:
            largest = ind
        if right < self.size and self.queue[right] > self.queue[largest]:
            largest = right
        if largest != ind:
            self.swap(ind, largest)
            self.maxHeapify(largest)

    def maximum(self) -> float | int | None:
        """Return the maximum element in the priority queue.

        Complexity O(1).If the heap is empty, return None.
        """
        return self.queue[0] if self.size > 0 else None

    def extractMax(self) -> float | int | None:
        """Extract the maximum element from the priority queue.

        Complexity O(log n).
        If the heap is empty, return None.
        """
        if self.size == 0:
            return None
        else:
            temp = self.queue[0]
            self.size -= 1
            self.queue[0] = self.queue[self.size]
            del self.queue[self.size]
            self.maxHeapify(0)
        return temp

    def insert(self, data: float | int) -> None:
        """Insert an element in the priority queue.

        Complexity O(log n).
        """
        self.queue.append(data)
        current = self.size
        parent = self.parent(current)
        while parent >= 0 and self.queue[current] > self.queue[parent]:
            self.swap(current, parent)
            current = parent
            parent = self.parent(current)
        self.size += 1
