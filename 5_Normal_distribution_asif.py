from sympy import var
var('loc scale size')


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


loc # - (Mean) where the peak of the bell exists.

scale # - (Standard Deviation) how flat the graph distribution should be.

size # - The shape of the returned array.



# Normal (Gaussian) Distribution
# Normal Distribution

x = random.normal(size=(2, 3))

print(x)

# Another example

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

# Visualization of Normal Distribution

sns.distplot(random.normal(size=1000), hist=False)

plt.show()



