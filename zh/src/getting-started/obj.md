# What is a better function?

_We need a way to tell us that a function is good._

Let's be honest, we are learning machine learning for some serious, important, big brain things. We want the model to be as good as possible at what it does. But what is good? 

```python
{{#include ../code/what_is_good.py}}
```

A clever way to say one model is better than another model is to compare those models. _Turns out, in math, it's illegal to compare different vectors (an array of numbers), so our options are limited to scalars (single numbers)._ But what scalar? 

## Loss

In machine learning, there are a lot of tasks tackling real world problems. Such as understanding images. Such as predicting the next champion team of the world cup. There are too many possibilities in the real world. To deal with that problem, scientists basically give up. They stop trying to create a new prefect model. Instead, they focus on a model that solves problems good enough. They use a scalar to determine how far away the model's prediction of a known problem is different from the right answer, it's very common to call the scalar **loss**.

The smaller the loss, the better the function is. Usually the loss is a positive number, but occasionally we see negative losses permitted in a problem. As long a smaller loss indicates a better function. To calculate loss, we define a **loss function**. _The loss function is defined to operate on the function itself (it's a function of function) and output how good the model is. Realistically though, the loss function operates on the output of the function and determines how good that output is._ To further clarify what I mean

### Loosely defined loss function (the one used in PyTorch, TensorFlow, etc):

```python
{{#include ../code/formal_loss.py:6:11}}
```

### Formally defined loss function:

```python
{{#include ../code/formal_loss.py:14:26}}
```

We will talk about how to optimize the function in the next chapter.

In practice you often see the loosely defined loss function instead of the formally defined loss function. After all it's more flexible, and is better suited to be provided as a library function. However, since models and losses are discussed all together in the optimization phase, we will use the formally defined loss function in this book.

## Several commonly used loss functions:

### Mean absolute error:

Used in classification as well as regression problems.

Formula:

\\[L(x, y) = \sum_{i=1}^n |x_i - y_i|\\]
\\[x, y \in R^n \\]

Code:

```python
{{#include ../code/mae_loss.py:5:}}
```

### Mean squared error:

Used in classification as well as regression problems.

Formula:

\\[L(x, y) = \sum_{i=1}^n (x_i - y_i)^2\\]
\\[x, y \in R^n \\]

Code:

```python
{{#include ../code/mse_loss.py:5:}}
```

#### Cross-entropy loss:

Used in classification problems only.

Formula:

\\[L(x, y) = - \sum_{i=1}^n x_i \log_2 y_i\\]
\\[x_i, y_i \in [0, 1] \\]

Code:

```python
{{#include ../code/ce_loss.py:5:}}
```

## Summary

To define a good function, we have to **find the loss that for this function**. . To find the loss of a function, we **use a loss function to find out the loss**. **A good loss function shows far how the output of the model is from a good output**.
