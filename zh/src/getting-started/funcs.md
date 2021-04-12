
# Using models to make predictions

_In machine learning we want to build a model (a function) to do what we want._

You must have heard of machine learning models doing amazing things. But what exactly is a model? A model takes in some input and spit out some output. They are like functions we write in programs. You might have heard that some machine learning models know how to read a picture and translate them into words. In this case the input is the picture, and the output is the content of a picture in words we understand. Or maybe you have heard of how models can predict the stock market (while this is true, it's not that useful since the prediction may not be accurate, or else data scientists get so rich they no longer do data science), in such case the input previous days or years of share prices, the output tomorrow's share price.

```python
{{#include ../code/ml_model.py:4:}}
```

The possibilities of different uses of models is endless. But there are only _2 kinds_ of models, **classification**, and **regression**. What are those things?

## Classification

_Given some input, we want to separate those input data into different classes._

A concrete example of the above sentence: Suppose that we have several pictures of dogs and cats, and we want to separate them into two piles. One pile for dogs, and the other for cats. In machine learning, we could simply train a **classification model**, and the image is transformed by the model into two categories, dogs and cats. This task is called **classification** by us super smart machine learning masters.

```python
{{#include ../code/cat_dog.py:4:}}
```

In the above example, since there are only two categories, we can easily use a number to represent our confidence in the input being one of the classes, cats. The problem is referred to as a **binary classification problem**. However, what happens when there are more than two categories?

```python
{{#include ../code/cat_dog_rabbit.py:5:}}
```

We use an array to represent probabilities of different classes. It's usually called a **categorical classification problem**. To identify if a problem is a classification problem, think this: _am I predicting classes?_

## Regression

_Given some input, we want to predict the score of the input data._ Usually, the score is unbounded.

A concrete example of the above sentence: Suppose that we have an image of a star. We want to predict how hot is the surface (since we data scientists don't study physics and machine learning is cooler anyways), how are we going to do it?

```python
{{#include ../code/star_temp.py:4:}}
```

The output may not even be scalar. It can be an array as well! Predicting scalar is much more common though. To tell part classification from regression, just keep this in mind: _regression predicts value._

## Summary

All problems in machine learning fall into 2 categories, _classification_ and _regression_. The difference is that _classification_ are used to predict different categories, while _regression_ is used to predict a value. Since classification is usually solved by predicting probabilities, a direct result is that the output of a classification model is often bounded, while a regression model is not.
