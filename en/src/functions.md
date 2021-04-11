
# Functions

In machine learning we are obsessed with building a model that does what we want. But what exactly is a model? Well, a model are just a fancy way of saying a function. Basically all models, and all functions, do is they take in an input and spit out an output. You probably have heard of some machine learning model know how to read a picture and translate them into words. In this case the input is the picture, and the output is the content of a picture in characters. Or you heard of how models can predict the stock market (while this is true, it's not that useful since the prediction may not be accurate, or else you'll see a lot of rich data scientists), in such case the input previous days or years of share prices, the output tomorrow's share price or any time in the future, you get the idea.

The possiblities of different uses of functions is endless. But there are only _2 kinds_ of functions, **classification**, and **regression**. What are those things?

## Classification

_Given an input, we want to separate those input into different classes._

A concrete example of the above sentence: Suppose that we have several pictures of dogs and cats, and we want to separate them into two piles. One pile for dogs, and the other for cats. In machine learning, we could simply train a **classification model**, and the image is transformed by the model into two categories, dogs and cats. This task is called **classification** by us super smart machine learning masters.

```python
{{#include ./code/cat_or_dog.py}}
```

In the above example, since there are only two categories, we can easily use a number to represent our confidence in the input being one of the classes, cats. The problem is reffered to as a **binary classification problem**. However, what happens when there are more than two categories?

```python
{{#include ./code/cat_dog_rabbit.py}}
```

We use an array to represent probablities of different classes. It's usually called a **categorical classification problem**. To identify if a problem is a classification problem, think this: _am I predicting classes?_

## Regression

_Given an input, we want to predict the score of the input. The score is normally unbounded, or it could be more easily modeled as a binary classification problem._

A concrete example of the above sentence: Suppose that we have an image of a star. We want to predict how hot is the surface (since we data scientists don't study physics and machine learning is cooler anyways), how are we going to do it?

```python
{{#include ./code/star_temp.py}}
```

The output may not even be scalar. It can be an array as well! Predicting scalar is much more common though. To tell part classificatio from regression, just keep this in mind: _regression predicts value._

## Summary

There are mainly 2 kinds of functions to model all the problems we will face in machine learning, _classification_ and _regression_. The difference is that _classification_ are used to predict different categories, while _regression_ is used to predict a value. Since classification is usually solved by predicting probablities, a direct result is that the output of a classification model is often bounded, while a regression model is not.
