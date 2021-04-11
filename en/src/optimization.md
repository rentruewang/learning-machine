# Optimization

We have now have a function. We now what a good function is. Now, how do we get there? A naive way of trying to achieve that is to randomly choose parameters and cross our finger and hope that the function is good enough. However, the number of possible parameters is crazily large, so it's not a feasible solution. So how are the problem solved?

## Gradient Descent

Imagine you are standing on a hill. You want to find the lowest point in your region, how would you do it? You take a ball, and roll it down the hill, and naturally the ball stops at the place where the height is minumum. This is exactly what mathematicians decided to use to solve the problem. And it has a cool name. **Gradient descent**.

Wait, you ask. How is this rolling downhill related to gradient descent? Well, let's define a function which we want to optimize \\(f\\), and we define

\\(z = f(x, y)\\), given that \\(z, x, y \in R \\)

In other words, given there is a location on the 2D plane \\(xy\\), the function takes in the position and output a scalar. If we say that the scalar is the height at \\((x, y)\\), then if we plot \\((x, y, z)\\) in our head, it looks like a terrain. And if we "roll a ball" down from any location, the ball is eventually going to find a minimum (because of physics).

Now let's generalize the idea. Imagine our function \\(f\\) is no longer limited to 2 inputs. Let's substitute \\(f\\) for a loss function \\(L\\) we discussed last chapter (the formal one). 

The input is a function \\(f\\) that we want to optimize (the ball that we want to roll down the hill), and a pair of inputs \\((x, y)\\), given that \\(n \in N\\), \\(x, y \in R^n\\)

Remember that we've said over and over that the function is determined by it's parameters? To optimize a function, we optimize its parameter. In this case, **the function parameters** is the position of the ball, and the **loss function output** is the value we want to minimize.

```python
{{#include ./code/optimize_function.py}}
```

Now we get to the gradient part. _You can think of gradient as the steepest way uphill._ If you move along the gradient, you can increase the function value, in this case, the **loss function output** the fastest. So usually we want to move in the opposite direction (remember we are minimizing the function?). If we always move to the opposite direction of the gradient, we call this **stochastic gradient descent**.

### Stochastic Gradient Descent

Stochastic gradient descent is the most common gradient descent method, and the most basic one. It involves only 3 varaibles, \\(x, y, lr, iter\\). \\(x\\) is your input variable, \\(y\\) is your output variable, and \\(lr\), learning rate, is a scalar showing how far you can move in one iteration. You repeat for \\(iter\\) iterations. For the ultimate quality we would want \\(lr\\) to be as small as possible (to not jump too far because you want to follow the terrain), and as many \\(iter\\) as possible (to ensure that the minimum is obtained). But it's not possible to do so in practice. Selecting \\(lr\\) and \\(iter\\) has become more art than science, and is often called **hyperparameter tuning** (parameter is for functions).

```python
{{#include ./code/x_square_sgd.py}}
```

## Summary

We choose an initial **function** by selecting a parameter (randomly), then optimize it by gradient descent, the value we want to reduce is the output of the **loss function**, and the parameters we want to choose is the **function's parameters**. Gradient descent is a lot like rolling balls down the hills, in which the ball will find the lowest point, which is the minimum.
