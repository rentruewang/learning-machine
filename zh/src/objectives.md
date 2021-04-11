# Objectives

After we have looked into the basic categories of machine learning functions, we want to ask ourselves a question. Since there are just an astronomical number of functions even the most basic models can represent (because every change in parameter can yeild a totally different function, we'll cover parameters of deep learning functions later), how do we know which function is the best one? _Turns out, in math, it's illegal to compare different vectors (an array of numbers), so our options are limited to scalars (single numbers)._ But what scalar?

## Loss

In machine learning, there are a lot of tasks tackling real world problems. Such as understanding images. Such as predicting the next champion team of the world cup. There are too many possibilities in the real world. To deal with that problem, scientists basically give up. They stop trying to create a new prefect model. Instead, they focus on a model that solves problems good enough. They use a scalar to determine how far away the model's prediction of a known problem is different from the right answer, it's very common to call the scalar **loss**.

The smaller the loss, the better the function is. Usually the loss is a positive number, but ocassionaly we see negative loss premitted in a problem. As long a smaller loss indicates a better function. To calculate loss, we define a **loss function**. This loss function is a function used to calculate loss, as the name suggests.

## Several commonly used loss functions:

### Mean absolute error:

Used in classification as well as regression problems.

Formula:

\\[ L(x, y) = \sum_{i=1}^n |x_i - y_i|\ \ \  x, y \in R^n \\]

Code:

```python
{{#include ./code/mae_loss.py}}
```

### Mean squared error:

Used in classification as well as regression problems.

Formula:

\\[ L(x, y) = \sum_{i=1}^n ||x_i - y_i||_2\ \ \  x, y \in R^n \\]

Code:

```python
{{#include ./code/mse_loss.py}}
```

#### Crossentropy loss:

Used in classification problems only.

Formula:

\\[ L(x, y) = - \sum_{i=1}^n x_i \log_2 y_i \ \ \ x_i, y_i \in [0, 1] \\]

Code:

```python
{{#include ./code/ce_loss.py}}
```

## Summary

To define a good function, we have to **find the loss that for this function**. To find the loss of a function, we **use a loss function to find out the loss**.
