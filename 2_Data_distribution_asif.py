from numpy import random

# Random Distribution

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

# Another example

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size = (3, 5))

print(x)






