"""Priority queue interface."""

from dataclasses import dataclass
from typing import Protocol


@dataclass
class PriorityQueueInterface(Protocol):
    """Priority queue interface protocol."""

    size: int
    """Size of the priority queue."""

    def insert(self, data: float | int) -> None:
        """Insert an element in the priority queue."""
        ...

    def extractMax(self) -> float | int | None:
        """Extract the maximum element from the priority queue.

        Returns None if the list is empty.
        """
        ...
