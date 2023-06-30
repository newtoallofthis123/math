# Probability

Probability is basically how much we are sure that an event will occur. This is usually expressed as a number between 0 and 1. 0 means that the event will never occur and 1 means that the event will always occur.

## Likelihood vs Probability

Likelihood and probability are generally used interchangeably, but they are not the same thing.

Probability is about quantifying predictions of events yet to happen, whereas likelihood is measuring the frequency of events that already occurred.
Boardly speaking, probability is about the future, whereas likelihood is about the past.

## Probability and Odds

Probability and odds are also used interchangeably, but they are not the same thing.

Probability is the likelihood of an event occurring divided by the number of possible outcomes. Odds are the likelihood of an event occurring divided by the likelihood of an event not occurring.

Mathematically, the relationship between probability and odds is:

$Odds = \frac{Probability}{1 - Probability}$

or

$Probability = \frac{Odds}{1 + Odds}$

So, that means

$Probability = \frac{in favor}{total}$

$Odds = \frac{in favor}{against}$

So, for example, let's say that the probability of an event occurring is $\frac{1}{3}$. Then, the odds of that event occurring are $\frac{1}{2}$.
Since the probability of an event occurring is $\frac{1}{3}$, that means that the probability of an event not occurring is $\frac{2}{3}$. So, the odds of an event not occurring are $\frac{2}{1}$.

So, speaking in english, the odds are 2 to 1 that the event will not occur.

## Probability and Statistics

Probability and statistics are also used interchangeably, but they are not the same thing.

Probability is about quantifying predictions of events yet to happen, whereas statistics is about analyzing data that already happened.

## The Math of Probability

The math of probability is based on set theory. So, let's start with some definitions.

### Sample Space

The sample space is the set of all possible outcomes of an experiment. It is usually denoted by the greek letter $\Omega$.

### Event

An event is a subset of the sample space. It is usually denoted by the capital letter $E$.

### Probability Definition

The probability of an event is the number of elements in the event divided by the number of elements in the sample space.

$P(E) = \frac{|E|}{|\Omega|}$

### Probability Axioms

The probability of an event is always between 0 and 1.

$0 \leq P(E) \leq 1$

The probability of the sample space is 1.

$P(\Omega) = 1$

The probability of the union of two events is the sum of the probabilities of the events minus the probability of the intersection of the events.

$P(E \cup F) = P(E) + P(F) - P(E \cap F)$

The probability of the complement of an event is 1 minus the probability of the event.

$P(E^c) = 1 - P(E)$

## Things in Probability

### Joint Probability

The joint probability of two events is the probability of the intersection of the two events.

$P(E \cap F)$

So, for example, let's say that we have a bag with 3 red balls and 2 blue balls. We pick a ball at random. What is the probability that the ball is red and blue?

$P(Red \cap Blue) = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10}$

Hence, boardly speaking, the probability of two events occurring is the probability of the first event occurring times the probability of the second event occurring.

Matheatically, the relationship between joint probability and probability is:

$P(E \cap F) = P(E) \times P(F)$
