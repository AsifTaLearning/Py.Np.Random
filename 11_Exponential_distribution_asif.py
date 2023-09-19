from sympy import var
var('scale size')

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

scale # - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

size # - The shape of the returned array.

x = random.exponential(scale=2, size=(2, 3))

print(x)

# Visualization of Exponential Distribution

sns.distplot(random.exponential(size=1000), hist=False)

plt.show()




