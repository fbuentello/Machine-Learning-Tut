# Hierarchical Clustering = Let machine choose what clusters to use.
import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

centers = [[1,1],[5,5],[3,10]]

# Were using _(Underscore) to say this var is not important
# _ = labels used in the generated dataset
# Change cluster_std
X , _ = make_blobs(n_samples=500, centers=centers, cluster_std=1)

plt.scatter(X[:,0],X[:,1])
plt.show()

ms = MeanShift()

ms.fit(X)
# Labels = the Labels the machine assigned to the data
labels = ms.labels_

# The estimated centers
cluster_centers = ms.cluster_centers_

print(cluster_centers)

#np.unique = how many unique variables exist
n_clusters_ = len(np.unique(labels))

print("Number of estimated clusters:", n_clusters_)

colors = 10*['r.','g.','b.','c.','k.','y.','m.']
print(colors)
print(labels)

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)



plt.scatter(cluster_centers[:, 0],
            cluster_centers[:,1],
            marker = "x",
            s=150,
            linewidths=5,
             zorder=10)

plt.show()
