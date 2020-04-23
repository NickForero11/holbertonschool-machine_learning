#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

# Create 3D Layout
fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(1, 1)
ax = fig.add_subplot(gs[0, 0], projection='3d')

# Set 3D axes data and color configuration
axes = np.hsplit(pca_data, 3)
color_data = {'c': labels, 'cmap': plt.cm.plasma}

# Plot Axes
ax.scatter(*axes, **color_data)

# Set Labels
ax.set_xlabel('U1', labelpad=15)
ax.set_ylabel('U2', labelpad=15)
ax.set_zlabel('U3', labelpad=15)
plt.title('PCA of Iris Dataset', pad=25)

plt.show()
