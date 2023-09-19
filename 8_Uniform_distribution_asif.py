from sympy import var
var('a b size')

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# Uniform Distribution

a # - lower bound - default 0 .0.

b # - upper bound - default 1.0.

size # - The shape of the returned array.


x = random.uniform(size=(2, 3))

print(x)

# Visualization of Uniform Distribution

sns.distplot(random.uniform(size=1000), hist=False)

plt.show()




