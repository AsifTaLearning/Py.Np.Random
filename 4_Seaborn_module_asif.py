# import matplotlib

import matplotlib.pyplot as plt

# Import Seaborn

import seaborn as sns

# Plotting a Distplot

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()

# Plotting a Distplot Without the Histogram

sns.distplot([0, 1, 2, 3, 4, 5], hist = False)

plt.show()



