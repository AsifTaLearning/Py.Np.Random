from sympy import var
var('df size')

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# Chi Square Distribution

df # - (degree of freedom).

size # - The shape of the returned array.

x = random.chisquare(df=2, size=(2, 3))

print(x)

# Visualization of Chi Square Distribution

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()



