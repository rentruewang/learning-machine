def distance(x, y):
    """
    This function is for calculating the distance between x and y
    In this case, it's the squared-euclidean distance
    """
    return ((x - y) ** 2).sum()


def loss_func(F, real_x, real_y):
    """
    loss_func calls the function for you,
    and evaluate how far in the model's output to the correct output.
    """

    pred_y = F(real_x)
    loss = distance(pred_y, real_y)

    # Optimize the function based on loss
    optimize_function(F)

    return loss


def optimize_function(F):
    "We are doing something to `F`'s parameter and hope that the function gets better"
    F.parameter = 0
