from sympy import var
var('scale size')

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# Rayleigh Distribution

scale # - (standard deviation) decides how flat the distribution will be default 1.0).

size # - The shape of the returned array.

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

# Visualization of Rayleigh Distribution

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()



