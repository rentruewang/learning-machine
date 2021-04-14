import numpy as np


def ce_loss(x, y):
    "CE: Cross entropy. You will learn about this later."
    return -(x * np.log2(y)).sum()
