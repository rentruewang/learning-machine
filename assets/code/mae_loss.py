import numpy as np
from numpy import ndarray


def mae_loss(x: ndarray, y: ndarray) -> float:
    "MAE: mean absolute error. Mean of absolute difference."
    return np.abs(x - y).mean().item()
