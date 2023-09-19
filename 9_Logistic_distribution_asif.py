from sympy import var
var('loc scale size')

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# Logistic Distribution

loc # - mean, where the peak is. Default 0.

scale # - standard deviation, the flatness of distribution. Default 1.

size # - The shape of the returned array.

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)

# Visualization of Logistic Distribution

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()

# Difference Between Logistic and Normal Distribution

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()





