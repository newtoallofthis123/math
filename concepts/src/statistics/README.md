# Descriptive and Inferential Statistics

Statistics is the heart of data driven decision making. It is a branch of mathematics that deals with the collection, analysis, interpretation, and presentation of masses of numerical data.

Data in itself is not useful. It is the interpretation of data that leads to knowledge and wisdom. Statistics is the science of learning from data. It is the art of extracting knowledge from data.
The way to envision data is to think of them like snapshots of reality. Data are the facts and figures collected, analyzed, and summarized for presentation and interpretation.

## Descriptive vs Inferential Statistics

Descriptive statistics is the branch of statistics that involves the organization, summarization, and display of data. Descriptive statistics describes data through numerical summaries, tables, and graphs. The goal of descriptive statistics is to describe the data in a way that is understandable and meaningful.

Inferential statistics is the branch of statistics that involves using a sample to draw conclusions about a population. Inferential statistics uses probability to make inferences about a population. The goal of inferential statistics is to draw conclusions about a population based on a sample.

## Few Important Terms

1. **Population**: A population is the entire group of individuals or objects to be studied. The population is the complete collection to be studied; it includes all subjects of interest. The population is the entire group of individuals or objects to be studied.

2. **Sample**: A sample is a subset of the population that is being studied. A sample is a subset of the population that is being studied.
For example, isn't it easier to count the number of people in a classroom than to count the number of people in a city? The classroom is the sample and the city is the population.

3. **Parameter**: A parameter is a numerical measurement describing some characteristic of a population.

4. **Bias**: Bias is the tendency of a measurement process to over- or under-estimate the value of a population parameter. It is the skewing of data in a particular direction, away from the true value. There is this tendency in which particular groups is more likely to include themselves in a sample and is known as self-selection bias.

## Descriptive Statistics

### Measures of Central Tendency

Measures of central tendency are measures that locate the center of a distribution of data. The mean, median, and mode are the three most commonly used measures of central tendency.

### Mean and Weighted Mean

Mean is the average of a set of values. As simple as that. The operation is also quite simple. You add up all the values and divide by the number of values. The mean is the most commonly used measure of central tendency. It is the arithmetic average of a set of values. The mean is the sum of the values divided by the number of values.

$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

Weighted mean on the other hand doesn't give an equal weight to all the values. It is the sum of the product of the values and their weights divided by the sum of the weights.

$$\bar{x} = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}$$

The weight is determined by the magnitude of the value. The larger the value, the larger the weight. The smaller the value, the smaller the weight.

To calculate the weights,

$$w_i = \frac{x_i}{\sum_{i=1}^{n} x_i}$$

Hence effectively,

$$\bar{x} = \frac{\sum_{i=1}^{n} x_i^2}{\sum_{i=1}^{n} x_i}$$

### Median

The median is the midpoint of a distribution of data. It is the value that divides the data into two equal parts. Half the values are less than or equal to the median and half the values are greater than or equal to the median. The median is the middle value when the data are arranged in order of increasing magnitude.

Medians are particularly useful when the data are skewed. The median is the middle value when the data are arranged in order of increasing magnitude.

> Media is a quantile. That means it cuts 50% of the data. The median is the 50th percentile. Whereas we also have others like quartiles (25th, 50th, 75th) and deciles (10th, 20th, 30th, 40th, 50th, 60th, 70th, 80th, 90th).

### Mode

Mode is the value that occurs most frequently in a data set. A data set can have more than one mode. A data set with two modes is called bimodal. A data set with more than two modes is called multimodal.

## Variance and Standard Deviation

Variance of a data set defines how much the data is spread out. It is the average of the squared differences from the mean.

So, for example if we have a data like this

|  Value | Mean  | Difference  |
|---|---|---|
| 0  |  6.51 | -6.51  |
| 1  | 6.51  | -5.51  |
| 5  | 6.51  |  -1.51 |
| 7  | 6.51  | 0.49  |
| 9  | 6.51  |  2.49 |
| 10  |  6.51 | 3.49  |
| 14  | 6.51 | 8.49  |

Now, if we take the average of the differences, we get 0. So, we can't use the average of the differences to measure the spread of the data. So, we take the average of the squared differences. This is called variance.

$$\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}$$'

The square root of the variance is called the standard deviation.
Standard deviation sort of has the variance
scaled to the measure of the data. So, it is more useful than variance.

$$\sigma = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}}$$

When we calculate these values, we are calculating the population variance and population standard deviation. When we calculate the variance and standard deviation of a sample, we are calculating the sample variance and sample standard deviation.

The sample variance is the sum of the squared differences between each value and the mean divided by the number of values minus one.

$$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$$

By calculating one value short of the total number of values, we are able to get a better estimate of the population variance since it increases the variance.

## The Normal Distribution

The most important bell curve in all of probability and statistics is the normal distribution. Also called the gaussian distribution, it is a continuous distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean.

Properties of the normal distribution:

- The mean, mode and median are all equal.
- It's perfectly symmetrical.
- The curve never touches the x-axis.
- It has more mass in the center than in the tails.

## Probability Density Function

The probability density function (PDF) of a continuous random variable is a function that describes the relative likelihood for this random variable to occur at a given point. The probability for the random variable to fall within a particular region is given by the integral of this variable’s density over the region.

So, pdf goes in hand with calculating the binomial distribution and the normal distribution.

The probability density function of the normal distribution is:

$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} (\frac{x-\mu}{\sigma})^2}$$

where $\mu$ is the mean and $\sigma$ is the standard deviation of the distribution. The variance of the distribution is $\sigma^2$. A random variable with a Gaussian distribution is said to be normally distributed and is called a normal deviate.

This can be quite daunting to calculate by hand. 
We mostly use `scipy.stats.norm` to calculate the pdf.

```python
from scipy.stats import norm
norm.pdf(0)
```

## Cumulative Distribution Function

The CDF basically represents the probability that a random variable X will take a value less than or equal to x. It is the integral of the PDF.

$$F(x) = \int_{-\infty}^{x} f(t) dt$$

This is similar to what we did with the beta distribution.

## Z-Score

The z-score is the number of standard deviations by which the value of a raw score (i.e., an observed value or data point) is above or below the mean value of what is being observed or measured.

$$z = \frac{x - \mu}{\sigma}$$

The z-score is positive if the value lies above the mean, and negative if it lies below the mean. If the z-score is zero, it means the value is equal to the mean.

# Inferential Statistics

## Central Limit Theorem

The central limit theorem states that the sampling distribution of the mean of any independent, random variable will be normal or nearly normal, if the sample size is large enough.

So, if we take a sample of size n from a population with mean $\mu$ and standard deviation $\sigma$, then the sampling distribution of the sample mean $\bar{x}$ will have mean $\mu$ and standard deviation $\frac{\sigma}{\sqrt{n}}$.

So, it is no longer n-1, but $\sqrt{n}$. This is important since it helps us infer the population mean from the sample mean.

Normally, you need 31 samples to get a normal distribution. But, if the population is normal, then you can get a normal distribution with any sample size.

## Confidence Intervals

A confidence interval is a range of values above and below a point estimate that captures the true population parameter at some predetermined confidence level.

So, if we have a sample mean $\bar{x}$, then the confidence interval is given by

$$\bar{x} \pm z^* \frac{\sigma}{\sqrt{n}}$$

where $z^*$ is the z-score for the confidence level.

However, first we must define the `level of confidence`. This is the probability that the confidence interval actually contains the population mean. So, if we have a confidence level of 95%, then there is a 95% chance that the confidence interval contains the population mean.
This is also called as LOC.

Getting the critical value for a given confidence level is easy. We can use `scipy.stats.norm.ppf` to get the critical value.

```python
from scipy.stats import norm

def critical_value(loc):
    norm_dist = norm(loc=0, scale=1)
    left_tail = (1 - loc) / 2
    upper_tail = 1 - left_tail
    return norm_dist.ppf(upper_tail), norm_dist.ppf(left_tail)

critical_value(0.95)
```

<!-- !TODO -->
---TO BE CONTINUED---