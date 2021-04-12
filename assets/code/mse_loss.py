import numpy as np
from numpy import ndarray


def mse_loss(x: ndarray, y: ndarray) -> float:
    "MSE: mean absolute error. Mean of squared difference."
    return np.power(x - y, 2).mean().item()
