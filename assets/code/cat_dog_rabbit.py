import numpy as np


def cat_dog_rabbit(image):
    """
    There are three categories. Cats. Dogs. Rabbits.
    So normally we will output an array of length 3 showing how possible the input is of each class.
    Do note that the array sums to 1 because the sum of probablities of all possible cases is 1.
    """
    return np.array([0.6, 0.2, 0.2])
