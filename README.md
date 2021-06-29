# learning-machine

**[Straitforward machine learning based on answers and intuition for machine learners](https://rentruewang.github.io/learning-machine)**

[![Website](https://github.com/rentruewang/learning-machine/actions/workflows/github-pages.yaml/badge.svg)](https://github.com/rentruewang/learning-machine/actions/workflows/github-pages.yaml)

_**Whoever fights monsters should see to it that in the process he does not become a monster. And if you gaze long enough into an abyss, the abyss will gaze back into you. And in order to tame machine learning, one mush first know how to learn machine.**_
--- Me, 2021

## Why this book?

There are many resources for machine learning on the internet. However, most of them are either

1. Too long. It takes half an hour just to read through.

2. Too math heavy. It takes you forever to understand.

3. Too confusing. The concepts are not strait-forward.

This book aims to solve all of that. It tries to be as concise but easy to grasp as possible.

## Who is this book for?

This book is for learners who want to quickly grasp an idea, without really dive into a topic (it takes way too long!). The book is a handbook for people who want to preserve their time.

### Disclaimer

This book assumes that you have at least some basic understanding of programming.

## Contributing

We take openness and inclusiveness very seriously. We have adopted the following code of conduct.

[Contributor Code of conduct](CODE_OF_CONDUCT.md)

## Index

### [Introduction](book/intro.ipynb)

- [Getting Started](book/basic/basic.ipynb)
  - [Approximation](book/basic/approx/approx.ipynb)
  - [Gradients](book/basic/gradients/gradients.ipynb)
    - [Are loss function differentiable?](book/basic/gradients/loss-fn-derivative.ipynb)
- [Common Tasks](book/tasks/tasks.ipynb)
  - [Regression](book/tasks/regression/regression.ipynb)
    - [Expectation Maximization Algorithm](book/tasks/regression/em-algo.ipynb)
  - [Classification](book/tasks/classification/classification.ipynb)
    - [Gaussian Mixture Model](book/tasks/classification/gmm.ipynb)
- [Common Building Blocks](book/layers/layers.ipynb)
  - [Linear Layer](book/layers/linear/linear.ipynb)
  - [Convolution Layer](book/layers/cnn/cnn.ipynb)
  - [Recurrent Layer](book/layers/rnn/rnn.ipynb)
  - [Embedding Layer](book/layers/emb/emb.ipynb)
  - [Dropout Layer](book/layers/dropout/dropout.ipynb)
  - [Normalization Layer](book/layers/norm/norm.ipynb)
  - [Padding Layer](book/layers/padding/padding.ipynb)
  - [Pooling Layer](book/layers/pooling/pooling.ipynb)
  - [Transformer Block](book/layers/transformer/transformer.ipynb)
    - [Attention Layer](book/layers/transformer/attn/attn.ipynb)
- [Generative Models](book/generative/generative)
  - [Auto Encoders](book/generative/ae/ae.ipynb)
    - [Variational Auto Encoders](book/generative/ae/vae/vae.ipynb)
  - [Generative Adversarial Networks](book/generative/gan/gan.ipynb)
