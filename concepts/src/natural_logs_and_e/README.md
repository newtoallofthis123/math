# Euler's Number and Natural Logarithms

## Euler's Number

Euler's number, represented by $e$ is a very important number in mathematics. It is approximately equal to $2.71828$.

It is a common mathematical constant and is used in many mathematical equations, primarily in calculus and analysis.

It is defined as the limit of $(1 + \frac{1}{n})^n$ as $n$ approaches infinity.

$e = \lim_{n \to \infty} (1 + \frac{1}{n})^n$

For a little proof of this, it's do something simple.
Let's substitute $n$ with $100$.

$e = \lim_{n \to \infty} (1 + \frac{1}{100})^{100}$

Now, when we calculate this, we get $2.70481$.
Now, let's say $n = 1000$.

$e = \lim_{n \to \infty} (1 + \frac{1}{1000})^{1000}$

Now, when we calculate this, we get $2.71692$.
When we continue this process, we get closer and closer to $2.71828$.

Hence, well we can't really prove it, we can say that it is approximately equal to $2.71828$.

### Why is it used so much?

The reasons why $e$ is used so much is because of its properties.
First it's derivative is itself and integral is also itself.
This makes mathematical equations much easier to solve.

Now, let's do this in python.

```python
import math

p = 100 # principal
r = 2.0 # percent
t = 2.0 # years
## Compound Interest
i = p * (math.e ** (r * t))
```

As simple as that.

## Natural Logarithms

When a logarithm is written with a base of $e$, like this:
$\log_e(x)$
Then it is said to be a natural logarithm.

As the name suggests, it is used in many natural phenomena, like population growth, radioactive decay, etc.
In fact in many programming languages, their mathematical abstraction by default uses $e$ as the base.
