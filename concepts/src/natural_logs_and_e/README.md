# Euler's Number and Calculus

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

## Limits

As we saw earlier, $e$ is defined as the limit of $(1 + \frac{1}{n})^n$ as $n$ approaches infinity.
Now this is quite an interesting thing.

Let's say we have a function $f(x) = \frac{1}{x}$.
Now, let's say we want to find the limit of this function as $x$ approaches infinity.

$\lim_{x \to \infty} \frac{1}{x}$

Now, we can't really substitute $x$ with infinity, so we'll have to do something else.
We'll have to substitute $x$ with a very large number, like $1000000$. Now, when we calculate this, we get $0.000001$.
When we keep increasing the value of $x$, we get closer and closer to $0$.
So, we can say that the limit of this function as $x$ approaches infinity is $0$.

$\lim_{x \to \infty} \frac{1}{x} = 0$

### Using Sympy to Calculate Limits

Now, let's use sympy to calculate the limit of this function as $x$ approaches infinity.

```python
from sympy import *

x = symbols('x')
limit(1/x, x, oo)
```

Now, when we run this, we get $0$.
If we plot the graph of this function, we get this.

![](/concepts/images/1_by_x_graph.png)

> PS: Use sympy to solve all your college math problems.

## Derivatives

Now, the natural consequence of limits is derivatives.
Derivatives are the rate of change of a function.
So, they are used to find the rate of change of a function at a particular point.

These are dynamic and are used in many real world applications, like finding the velocity of a car at a particular point, finding the acceleration of a car at a particular point, etc.

Now, let's say we have a function $f(x) = x^2$.
Now, let's say we want to find the derivative of this function at $x = 2$.

We use the formula:
$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$

This is called the first principle of derivatives.
Now, if we substitute $x$ with $2$, we get:

$f'(2) = \lim_{h \to 0} \frac{f(2 + h) - f(2)}{h}$

$=> f'(2) = \lim_{h \to 0} \frac{(2 + h)^2 - 2^2}{h}$

$=> f'(2) = \lim_{h \to 0} \frac{4h + h^2}{h}$

$=> f'(2) = \lim_{h \to 0} \frac{h(4 + h)}{h}$

$f'(2) = 4$

We can also use sympy to calculate the derivative of this function at $x = 2$.

```python
from sympy import *

x = symbols('x')
diff(x**2, x).subs(x, 2)
```

This is mathematically equivalent to saying that the slope of the tangent at $x = 2$ is $4$.
Or can be represented as:

$\frac{d x^2}{dx} = 2x$

Now sympy is great and stuff, but the actual way you can implement derivative in pure python is actually quite cool.

The way to do it, like most mathematical things in python is to use the base formula with random numbers.

```python
def derivative_cal(f, x, h):
    return (f(x + h) - f(x)) / h

def f(x):
    return x ** 2

print(derivative_cal(f, 2, 0.0001))
```

Now, when we run this, we get $4.0001$.
Which is pretty close to $4$ and I think that's pretty cool.

## Partial Derivatives

Now partial derivatives can be considered as the slope of a function in a particular direction, like the slope of a function in the $x$ direction or the slope of a function in the $y$ direction.

This would not be the same as the slope of the tangent at a particular point, but it would be the slope of the function in a particular direction.

Hence, if I have to calculate the partial derivative of a function $f(x, y)$ in the $x$ direction, I would have to calculate the derivative of the function with respect to $x$.

So, for example, let's say

$f(x, y) = 2x^3 + 3y^3$

Now, if I want to calculate the partial derivative of this function in the $x$ direction, I would have to calculate the derivative of this function with respect to $x$.
With respect to $x$, $y$ is a constant, so it would be treated as a constant.

$\frac{\partial f(x, y)}{\partial x} = 6x^2$

Similarly for y,

$\frac{\partial f(x, y)}{\partial y} = 9y^2$

Now, let's say we want to calculate the partial derivative of this function in the $x$ direction at $x = 2$ and $y = 3$.

$\frac{\partial f(x, y)}{\partial x} = 24$
$\frac{\partial f(x, y)}{\partial y} = 81$

Hence,

$\frac{\partial f(x, y)}{\partial x\partial y} = \frac{24}{81} = 0.296$

Now, let's use sympy to calculate the partial derivative of this function in the $x$ direction at $x = 2$ and $y = 3$.

```python
from sympy import *

x, y = symbols('x y')

f = 2 * x ** 3 + 3 * y ** 3

d_x = diff(f, x).subs([(x, 2), (y, 3)])
d_y = diff(f, y).subs([(x, 2), (y, 3)])

print(d_x / d_y)
```

Now, when we run this, we get
$\frac{24}{81} = 0.296$.

Plotting the graph of this function, using sympy, we get this

![2x^2 + 3y^3 Graph](/concepts/images/2x%5E2%2B3y%5E3_graph.png)

## Integrals

Now, integrals are the opposite of derivatives.
They are not like the exact opposite, but they are the opposite in the sense that they are used to find the area under a curve.

Derivatives give us a slice of the curve at a particular point, but integrals give us the area under the curve.

Now, let's say we have a function $f(x) = x^2$ and we want to find the area under the curve of this function from $x = 0$ to $x = 2$.

We can use the formula:
$\int_{0}^{2} x^2 dx$

This would give us the area under the curve. Now, we can use sympy to calculate this.

```python
from sympy import *

x = symbols('x')

integrate(x ** 2, (x, 0, 2))
```

Now, when we run this, we get $\frac{8}{3}$.

Now, let's get back to our function

$f(x, y) = 2x^3 + 3y^3$

Now, let's say we want to find the area under the curve of this function from $x = 0$ to $x = 2$ and $y = 0$ to $y = 3$.

Remembering our formula, we get:

$\int_{0}^{2} \int_{0}^{3} 2x^3 + 3y^3 dy dx$

Now, we can use sympy to calculate this.

```python
from sympy import *

x, y = symbols('x y')

f = 2 * x ** 3 + 3 * y ** 3

integrate(f, (y, 0, 3), (x, 0, 2))
```

Now, when we run this, we get $216$.

This is simple enough in python using sympy, but in actuality,
solving it on paper would be a lot more difficult.

![2x^3+3y^3 Graph](/concepts/images/2x%5E2%2B3y%5E3_graph.png)

The way it would work is you first take a small slice from the
curve in the $y$ direction, and then you take a small slice from the curve in the $x$ direction.
So, constructing a small rectangle, you would calculate the area of that rectangle and then you would add it to the total area.

The area of this tiny rectangle would be $dy*dx$.
Integrating over all the $y$ values, you would get the area of the curve in the $x$ direction and then integrating over all the $x$ values, you would get the area of the curve in the $y$ direction.

Mathematically, this would be represented as:

$\int_{x=0}^{x=2} \int_{y=0}^{y=3} 2x^3 + 3y^3 dy dx$

Hence, we can see that the order of integration matters.

## Gradient Descent

Now, gradient descent is a very important concept in machine learning.
Now, let's say we have a function $f(x) = x^2 + 2x + 1$ and we want to find the minimum of this function.

The way we can do this is by taking the derivative of this function and then finding the value of $x$ for which the derivative is $0$.

Hence,

$f'(x) = 2x + 2$

$=> 2x + 2 = 0$

$=> x = -1$

Hence, the minimum of this function is at $x = -1$.

That's pretty simple, but what if we have a function $f(x, y) = x^2 + y^2$ and we want to find the minimum of this function.

Now, we can't just take the derivative of this function with respect to $x$ and $y$ and then find the value of $x$ and $y$ for which the derivative is $0$.

We can't do this because we have two variables, $x$ and $y$.

So, what we can do is we can take the partial derivative of this function with respect to $x$ and $y$ and then find the value of $x$ and $y$ for which the partial derivative is $0$.

Hence,

$\frac{\partial f(x, y)}{\partial x} = 2x$

$\frac{\partial f(x, y)}{\partial y} = 2y$

$=> 2x = 0$

$=> x = 0$

$=> 2y = 0$

$=> y = 0$

Hence, the minimum of this function is at $x = 0$ and $y = 0$.
