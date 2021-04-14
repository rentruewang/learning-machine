def loss_func(x, y):
    "What does the terrain look like? It looks like a bowl, the closer to the center the lower."
    return ((x - y) ** 2).sum()


def sgd_once(x, y, lr):
    """
    sgd stands for stochastic gradient descent.
    It moves in the direct opposite of the gradient.
    lr means learning rate.
    It is a small number because we don't want to move too far in a step.
    """
    loss = loss_func(x, y)

    # This is the gradient descent step
    x -= lr * 2.0 * (x - y)

    new_loss = loss_func(x, y)

    # A successful step should mean that we get a smaller new loss
    assert new_loss < loss


def sgd(x: ndarray, y: ndarray, lr: float, iter: int):
    """
    A real sgd flow doesn't just make one step.
    It usually updates for several hundreds or even thousands of iterations
    """
    for _ in range(iter):
        sgd_once(x, y, lr)
