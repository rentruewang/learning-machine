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

    # If we are not happy with the function, do something to the parameter
    optimize_function(F)

    return practice_loss.practice_loss(predicted, sample_data.y)


def optimize_function(F: Callable):
    """
    We are doing something to `F`'s parameter and hope that the function gets better
    """
    F.parameter = 0
