"""Main file for the project."""

from dataclasses import dataclass, field  # dataclass, field useful for creating classes
# with default values and type hints
from enum import Enum
from timeit import default_timer as timer

import numpy as np
import pandas as pd  # pandas useful for creating dataframes
import plotly.express as px  # plotly useful for creating plots

from heap import Heap
from linked_list import LinkedList
from ord_linked_list import OrdLinkedList
from priority_queue_interface import PriorityQueueInterface


class InputType(Enum):
    """Select the type of input."""

    random = 1
    """Random input."""
    sorted = 2
    """Sorted input."""
    reversed = 3
    """Reversed input."""


class SelectQueueType(Enum):
    """Select the type of queue to use."""

    heap = 1
    """Heap implementation."""
    linked_list = 2
    """Linked list implementation."""
    ord_linked_list = 3
    """Ordered linked list implementation."""


@dataclass
class InputConfig:
    """Input configuration."""

    num_samples: int = 1000
    """Number of samples."""
    sample_range: tuple[int, int] = (0, 5000)
    """Range of the samples."""
    input_type: InputType = InputType.random
    """Type of input."""


@dataclass
class InputGenerator:
    """Input generator."""

    input_config: InputConfig = InputConfig()
    """Input configuration."""

    data: list[int] = field(init=False, default_factory=list)
    """Data to be used for the tests."""

    def __post_init__(self):
        """Initialize the data."""
        self.data = self._generate()

    def _generate(self) -> list[int]:
        """Generate the data."""
        match self.input_config.input_type:
            case InputType.random:
                data = np.random.randint(
                    self.input_config.sample_range[0],
                    self.input_config.sample_range[1],
                    self.input_config.num_samples,
                )
            case InputType.sorted:
                data = np.arange(self.input_config.num_samples)
            case InputType.reversed:
                data = np.arange(self.input_config.num_samples)[::-1]
            case _:
                raise ValueError("Invalid input type.")
        return data.tolist()


def insert_times(queue: PriorityQueueInterface, input_data: list[int]) -> pd.DataFrame:
    """Test the insert time."""
    ins_times = np.zeros(len(input_data))
    for ind, data in enumerate(input_data):
        start = timer()
        queue.insert(data)
        end = timer()
        ins_times[ind] = (end - start) / queue.size

    ins_times = np.cumsum(ins_times)

    return pd.DataFrame(
        data={
            "time": ins_times,
            "time_type": "Insertion",
            "sample_index": np.arange(len(input_data)),
        }
    )


def extract_times(queue: PriorityQueueInterface) -> pd.DataFrame:
    """Test the extract time."""
    n = queue.size
    indexes = np.arange(n)[::-1]
    extr_times = np.zeros(n)

    for ind in indexes:
        start = timer()
        queue.extractMax()
        end = timer()
        extr_times[ind] = (end - start) / (ind + 1)

    extr_times = np.cumsum(extr_times)

    return pd.DataFrame(
        data={
            "time": extr_times,
            "time_type": "Extraction",
            "sample_index": np.arange(n),
        }
    )


def queue_times(
        queue_type: SelectQueueType,
        input_gen: InputGenerator,
) -> pd.DataFrame:
    """Generate the times for the different queues.

    Args:
        queue_type: Type of queue to use.
        input_gen: Generator of the input data.

    Returns:
        A pandas DataFrame with the times.
    """
    queue: PriorityQueueInterface
    match queue_type:
        case SelectQueueType.heap:
            queue = Heap()
        case SelectQueueType.linked_list:
            queue = LinkedList()
        case SelectQueueType.ord_linked_list:
            queue = OrdLinkedList()
        case _:
            raise ValueError("Invalid queue type.")
    input_data = input_gen.data
    it = insert_times(queue=queue, input_data=input_data)
    et = extract_times(queue=queue)

    q_times_df = pd.concat([it, et], ignore_index=True)
    q_times_df["queue_type"] = queue_type.name
    q_times_df["input_type"] = input_gen.input_config.input_type.name
    return q_times_df


def compare_times() -> None:
    """Compare the time complexity of the different implementations."""
    input_config = InputConfig(
        num_samples=10000, sample_range=(0, 5000), input_type=InputType.random
    )
    input_gen = InputGenerator(input_config)
    df_heap_1 = queue_times(SelectQueueType.heap, input_gen)
    df_list_1 = queue_times(SelectQueueType.linked_list, input_gen)
    df_ord_list_1 = queue_times(SelectQueueType.ord_linked_list, input_gen)

    input_config.input_type = InputType.sorted
    input_gen = InputGenerator(input_config)
    df_heap_2 = queue_times(SelectQueueType.heap, input_gen)
    df_list_2 = queue_times(SelectQueueType.linked_list, input_gen)
    df_ord_list_2 = queue_times(SelectQueueType.ord_linked_list, input_gen)

    input_config.input_type = InputType.reversed
    input_gen = InputGenerator(input_config)
    df_heap_3 = queue_times(SelectQueueType.heap, input_gen)
    df_list_3 = queue_times(SelectQueueType.linked_list, input_gen)
    df_ord_list_3 = queue_times(SelectQueueType.ord_linked_list, input_gen)

    df_times = pd.concat(
        [
            df_heap_1,
            df_list_1,
            df_ord_list_1,
            df_heap_2,
            df_list_2,
            df_ord_list_2,
            df_heap_3,
            df_list_3,
            df_ord_list_3,
        ],
        ignore_index=True,
    )
    # figure = px.line(
    #     df_times,
    #     x="sample_index",
    #     y="time",
    #     color="time_type",
    #     title="100 elementi",
    #     facet_col="input_type",
    #     facet_row="queue_type",
    #     labels={"sample_index": "Numero di operazioni", "time": "Tempo", "input_type": "Tipo di input", "time_type": "Tipo di operazione", "queue_type": "Tipo di coda"},
    # )
    # figure = px.line(
    #     df_times,
    #     x="sample_index",
    #     y="time",
    #     color="input_type",
    #     facet_col="queue_type",
    #     facet_row="time_type",
    #     title="1000 elementi",
    #     labels={"sample_index": "Numero di operazioni", "time": "Tempo", "input_type": "Tipo di input", "time_type": "Tipo di operazione", "queue_type": "Tipo di coda"},
    # )

    figure = px.line(
        df_times,
        x="sample_index",
        y="time",
        color="time_type",
        facet_col="input_type",
        facet_row="queue_type",
        title="10000 elementi",
        labels={"sample_index": "Numero di operazioni", "time": "Tempo", "input_type": "Tipo di input",
                "time_type": "Tipo di operazione", "queue_type": "Tipo di coda"},
    )
    figure.update_layout(
        font=dict(
            family="Arial",
            size=24,  # Set the font size here
            color="Black"
        )
    )
    figure.show()
    # df_times["time"] = round(df_times["time"] * 1000000, 2)
    # df_times.query("sample_index == 999").to_latex("1000.tex")
    # df_times.query("sample_index == 9999").to_latex("10000.tex")


if __name__ == "__main__":
    compare_times()
