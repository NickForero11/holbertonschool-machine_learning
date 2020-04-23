#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Setup Data for plotting
labels = ("Farrah", "Fred", "Felicia")
colors = ("red", "yellow", "#ff8000", "#ffe5b4")
num_fruits = len(fruit)

# Set base level for the bars
bottom = [0, 0, 0]

# Plot bars
for idx in range(num_fruits):
    plt.bar(
        labels,
        fruit[idx],
        color=colors[idx],
        width=0.5,
        bottom=bottom
    )
    bottom += fruit[idx]

# Set text of the graph
plt.ylabel("Quantity of Fruit")
plt.yticks(range(0, 81, 10))
plt.ylim(0, 80)
plt.title("Number of Fruit per Person")
plt.legend(["apples", "bananas", "oranges", "peaches"])

# Show graph
plt.show()
