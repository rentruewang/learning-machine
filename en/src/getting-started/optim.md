# How to get a great function?

_Knowing how good something is is no good, unless we can get a good one._

We have a model. We know how good it is. Now, how do we find a good model? A naive way of trying to achieve that is to randomly choose parameters and cross our fingers and hope that the model is good enough. However, the number of possible parameters can be crazily large, so it's not always feasible solution. What is a good way to solve the problem?

## Gradient descent

Imagine you are standing on a hill. You want to find the lowest point in your region, how would you do it? You take a ball, and roll it down the hill, and naturally the ball stops at the place where the height is minimum. This is exactly what mathematicians decided to use to solve the problem. And it has a cool name. **Gradient descent**.

Wait, you ask. How is this rolling downhill related to gradient descent? Well, let's define a function which we want to optimize \\(f\\), and we define

\\[z = f(x, y)\\]
\\[z, x, y \in R\\]

In other words, given there is a location on the 2D plane \\(xy\\), the function takes in the position and output a scalar. If we say that the scalar is the height at \\((x, y)\\), then if we plot \\((x, y, z)\\) in our head, it looks like a terrain. And if we "roll a ball" down from any location, the ball is eventually going to find a minimum (because of physics).

Now let's generalize the idea. Imagine our function \\(f\\) is no longer limited to 2 inputs. Let's substitute \\(f\\) for a loss function \\(L\\) we discussed last chapter (the formal one). 

The input is a function \\(f\\) that we want to optimize (the ball that we want to roll down the hill), and a pair of inputs \\((x, y)\\), given that \\(n \in N\\), \\(x, y \in R^n\\)

Remember that we've said over and over that the function is determined by it's parameters? To optimize a function, we optimize its parameter. In this case, **the function parameters** is the position of the ball, and the **loss function output** is the value we want to minimize.

```python
{{#include ../code/formal_loss.py:14:}}
```

Now we get to the gradient part. Warning: A little math here.

First, let's talk about what gradients are. Note that the weird upside-down triangle is the notation for gradient.

Let's suppose there is a function.

\\[y = f(x_1, x_2, ... , x_n)\\]
\\[y, x_1, x_2 , ... , y_n, n \in R\\]

Then we say that the gradient of \\(y\\):

\\[\nabla y = \frac{\partial y}{\partial x} = (\frac{\partial y}{\partial x_1}, \frac{\partial y}{\partial x_2}, ..., \frac{\partial y}{\partial x_n})^T\\]

If we now make the dot product of \\(\nabla y\\) and  a small change in \\(x\\), denoted by \\(\Delta x\\), we observe:

\\[(\nabla y)^T(\Delta x) = \frac{\partial y}{\partial x_1}\partial x_1 + \frac{\partial y}{\partial x_2}\partial x_2 + ... + \frac{\partial y}{\partial x_n}\partial x_n = \sum_{i=1}^n \Delta y_i = \Delta y\\]

<!-- TODO: add more descriptions -->
The multiplication of the gradient of \\(y\\) and a small change in \\(x\\) yields the change in \\(y\\)! This is why gradients are so useful.

_You can think of gradient as the steepest way uphill._ If you move along the gradient, you can increase the function value the fastest, in this case, you will increase the **loss**. So usually we want to move in the opposite direction of the gradient at a point (remember we are minimizing the function?). If we always move to the opposite direction of the gradient, we will eventually get a (local) minimum value of the function, we call this **stochastic gradient descent**.

### Stochastic gradient descent

Stochastic gradient descent is the most common gradient descent method, and the most basic one. It involves only 3 variables, \\(x, y, lr, iter\\). \\(x\\) is your input variable, \\(y\\) is your output variable, and \\(lr\\), learning rate, is a scalar showing how far you can move in one iteration. You repeat \\(iter\\) iterations. For the ultimate quality we would want \\(lr\\) to be as small as possible (to not jump too far because you want to follow the terrain), and as many \\(iter\\) as possible (to ensure that the minimum is obtained). But it's not possible to do so in practice. Selecting \\(lr\\) and \\(iter\\) has become more art than science, and is often called **hyperparameter tuning** (parameter is for functions).

```python
{{#include ../code/x_square_sgd.py:6:}}
```

## Summary

We choose an initial **function** by selecting a parameter (randomly), then optimize it by gradient descent, the value we want to reduce is the **loss**, and the parameters we want to choose is the **function's parameters**. Gradient descent is a lot like rolling balls down the hills, in which the ball will find the lowest point, which is the minimum.
