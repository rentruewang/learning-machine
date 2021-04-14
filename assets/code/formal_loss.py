from typing import Callable

from numpy import ndarray


def distance(x: ndarray, y: ndarray) -> float:
    """
    This function is for calculating the distance between x and y
    In this case, it's the squared-euclidean distance
    """
    return ((x - y) ** 2).sum().item()


def loss_func(F: Callable, real_x: ndarray, real_y: ndarray) -> float:
    """
    loss_func calls the function for you,
    and evaluate how far in the model's output to the correct output.
    """

    pred_y = F(real_x)
    loss = distance(pred_y, real_y)

    # Optimize the function based on loss
    optimize_function(F)

    return loss


def optimize_function(F: Callable):
    "We are doing something to `F`'s parameter and hope that the function gets better"
    F.parameter = 0
