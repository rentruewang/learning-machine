# Linear Layer

```{note}
Sometimes, Linear Layers are also called Dense Layers, like in the toolkit Keras.
```

## What do linear layers do?

A linear layer transforms a vector into another vector. For example, you can transform a vector [1, 2, 3] to [1, 2, 3, 4] with a linear layer.

## When to use linear layers?

Use linear layers when you want to change a vector into another vector. This often happens when the target vector's shape is different from the vector at hand.

```{note}
Linear layers are often called linear transformation or linear mapping.
```

## How does a linear layer work?

There are two components in a linear layer. A weight $ W $, and a bias $ B $. If the input of a linear layer is a vector $ X $, then the output is $ W X + B $.

If the linear layer transforms a vector of dimension $ N $ to dimension $ M $, then $ W $ is a $ M \times N $ matrix, $ X $ is of dimension $ N $, $ B $ is of dimension $ M $.
