import numpy as np


def mae_loss(x, y):
    "MAE: mean absolute error. Mean of absolute difference."
    return np.abs(x - y).mean()
