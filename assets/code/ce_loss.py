import numpy as np
from numpy import ndarray


def ce_loss(x: ndarray, y: ndarray) -> float:
    "CE: Cross entropy. You will learn about this later."
    return -(x * np.log2(y)).sum().item()
