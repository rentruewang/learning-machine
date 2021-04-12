# Case Study: Linear models

We all know linear models. (Right...? Guys?) A linear model has the form \\(y = wx + b\\), with \\(x, y, w, b \in R\\). In data science though, a more fancy way to write this equation is \\(Y = WX + B\\), with \\(X \in R^m\\) \\(Y, B \in R^n\\), \\(W \in R^{mn}\\). You will need a little bit of linear algebra to understand this. Sorry. The reason scientists like to write things in matrix and vector form is that this way they can write a lot of equations in one place. Now we ask ourselves, where are the _Holy Trinity_ we just spent a lot of time on in previous chapters?

## 1. [Model](./funcs.md)

This one is simple. We define \\(F(X) = WX + B\\), with \\(X \in R^m\\), and \\(Y, B \in R^n\\), and \\(W \in R^{mn}\\). Then **\\(F\\) is our model**.

Code:

```python
{{#include ../code/linear_model.py:9:23}}
```

## 2. [Objective](./obj.md)

Suppose that we have some real data to evaluate our model on. If there's no real data then the model doesn't matter right? Suppose we have \\(R_X \in R^m\\), and \\(R_Y \in R^n \\) as our \\(X, Y\\) labels. We want to use **mean-squared-error** as our **loss function**. Then the **loss** of our function would be \\(\sum_{i=1}{n}({F_i(R_X)} - {R_Y}_i)^2\\).

Code:

```python
{{#include ../code/linear_model.py:25:41}}
```

## 3. [Optimization](./optim.md)

We want to find the gradient of the loss (\\(y\\) in the last chapter) with respect to the model parameters (\\(x\\) in the last chapter, `self.W`, `self.B` in the code). With a little aid of chain rule, we will find out the gradient of model output \\(Y\\) with respect to the model parameters \\(W, B\\).

In partial derivative form:

\\[\frac{\partial Y_i}{\partial W_{ij}} = X_j\\]
\\[\frac{\partial Y_i}{\partial B_i} = 1\\]

Since the loss \\(L\\) is defined as:

\\[l = \sum_{i=1}^n (Y_i - {R_Y}_i)^2\\]

The gradient of \\(L\\) with respect to the model parameters \\(W, B\) is (in partial derivative form):

\\[\frac{\partial L}{\partial W_{ij}} = \frac{\partial L}{\partial Y_i} \frac{\partial Y_i}{\partial W_{ij}} = (Y_i - {R_Y}_i)(X_j) \\]

\\[\frac{\partial L}{\partial B_i} = \frac{\partial L}{\partial Y_i} \frac{\partial Y_i}{\partial B_i} = (Y_i - {R_Y}_i)\\]

Voila! Finally we get the answer. In tool-kits like PyTorch or TensorFlow though, the action is performed automatically by building a graph. So we don't suffer from this pain every time we want to write a program!

Code:

```python
{{#include ../code/linear_model.py:43:}}
```

## Summary

We have seen how the three essential parts in a training procedure work. Hopefully by now you have a better understanding of how things work in machine learning fashion.
