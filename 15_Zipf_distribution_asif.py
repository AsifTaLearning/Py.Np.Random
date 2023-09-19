from sympy import var
var('a size')

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# Zipf Distribution

a # - distribution parameter.

size # - The shape of the returned array.

x = random.zipf(a=2, size=(2, 3))

print(x)

# Visualization of Zipf Distribution

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()




