from sympy import var
var('a size')

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# Pareto Distribution

a # - shape parameter.

size # - The shape of the returned array.

x = random.pareto(a=2, size=(2, 3))

print(x)

# Visualization of Pareto Distribution

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()




