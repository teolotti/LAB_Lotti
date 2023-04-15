"""Node class for priority queues."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Node:
    """Node class for priority queues."""

    priority: float | int
    """Priority of the node."""
    next: Node | None = field(init=False, default=None)
    """Next node. None if it is the last node."""

    def get_priority(self) -> float | int:
        """Get the priority of the node."""
        return self.priority

    def get_next(self) -> Node | None:
        """Get the next node."""
        return self.next

    def set_priority(self, new_data: float | int) -> None:
        """Set the priority of the node."""
        self.priority = new_data

    def set_next(self, new_next: Node | None) -> None:
        """Set the next node. None if it is the last node."""
        self.next = new_next
