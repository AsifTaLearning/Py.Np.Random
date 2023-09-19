from sympy import var
var('n p size')

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Binomial Distribution

n # -  number of trials.

p # -  probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

size # - The shape of the returned array.


x = random.binomial(n=10, p=0.5, size=10)

print(x)

# Visualization of Binomial Distribution

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()

# Difference Between Normal and Binomial Distribution

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()