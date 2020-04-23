#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Data for Graph 1
y0 = np.arange(0, 11) ** 3

# Data for Graph 2
mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

# Data for Graph 3
x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

# Data for Graph 4
x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

# Data for Graph 5
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create figure and set layout
fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(3, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[2, :])

# Plot graph 1
ax1.plot(1, 1, y0, '-r')
ax1.set_xlim(0, 10)

# Plot graph 2
ax2.scatter(x1, y1, c='m', marker='.')
ax2.set_xlabel('Height (in)', fontsize='x-small')
ax2.set_ylabel('Weight (lbs)', fontsize='x-small')
ax2.set_title("Men's Height vs Weight", fontsize='x-small')

# Plot graph 3
ax3.plot(x2, y2)
ax3.set_xlabel('Time (years)', fontsize='x-small')
ax3.set_ylabel('Fraction Remaining', fontsize='x-small')
ax3.set_title("Exponential Decay of C-14", fontsize='x-small')
ax3.set_xlim(0, 28650)
ax3.set_yscale("log")

# Plot graph 4
ax4.plot(x3, y31, '--r', x3, y32, '-g')
ax4.set_xlabel('Time (years)', fontsize='x-small')
ax4.set_ylabel('Fraction Remaining', fontsize='x-small')
ax4.set_title("Exponential Decay of Radioactive Elements", fontsize='x-small')
ax4.set_xlim(0, 20000)
ax4.set_ylim(0, 1)
ax4.legend(['C-14', 'Ra-226'], title_fontsize='x-small')

# Plot graph 1
ax5.hist(student_grades, bins=10, range=(0, 100), edgeColor='k')
ax5.set_xlabel("Grades", fontsize='x-small')
ax5.set_ylabel("Number of Students", fontsize='x-small')
ax5.set_xlim(0, 100)
ax5.set_ylim(0, 30)
ax5.set_xticks(range(0, 101, 10))
ax5.set_title("Project A", fontsize='x-small')

# Set title and display graph
plt.suptitle("All in One", fontsize='20')
plt.show()
