from sympy import var
var('n pvals size')

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# Multinomial Distribution

n # - number of possible outcomes (e.g. 6 for dice roll).

pvals # - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).

size # - The shape of the returned array.

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)




