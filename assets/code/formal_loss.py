from typing import Callable, NamedTuple

from numpy import ndarray

import practice_loss

Pair = NamedTuple("Pair", [("x", ndarray), ("y", ndarray)])


def formal_loss(F: Callable, sample_data: Pair) -> float:
    """
    formal_loss calls the function for you,
    and evaluate how far in the model's output to the correct output.
    """

    predicted = F(sample_data.x)
    return practice_loss.practice_loss(predicted, sample_data.y)
