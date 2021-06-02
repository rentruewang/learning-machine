# Do loss functions have to be differentiable?

Yes and no. If the loss function is only used for evaluating the quality of the prediction (on an evaluation set), then it does not have to be differentiable. However, if the loss function is the objective of a gradient descent algorithm, then yes, it has to be differentiable to do that.

<!-- TODO: Detailed explanation. -->
