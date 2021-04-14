import numpy as np


def mse_loss(x, y):
    "MSE: mean absolute error. Mean of squared difference."
    return np.power(x - y, 2).mean()
