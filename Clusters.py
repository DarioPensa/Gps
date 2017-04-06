import numpy as np
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2
import pandas as pd
import matplotlib.pyplot as plt
from pylab import plot,show
from sklearn.cluster import AffinityPropagation,SpectralClustering
from itertools import cycle
from sklearn.preprocessing import normalize
'''
features = []


geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
sensorLog=open(geo_dir+'\TireForTruck\Merged5000007.csv')
Reader=pd.read_csv(sensorLog)

for index, row in enumerate(Reader['Lat']):
    features.append((row,Reader['Long'][index]))

print features
FArray=np.asarray(features)
centroids,closest_centroid=kmeans2(FArray,8)
print centroids

# assign each sample to a cluster
idx= vq(FArray,centroids)

plt.figure(figsize=(100, 50), dpi=100)
plt.scatter(FArray[:,0], FArray[:,1], c=closest_centroid, s=100)
show()
'''
def K_means(points):
    FArray = np.asarray(points)
    centroids, closest_centroid = kmeans2(FArray, 8)

    # assign each sample to a cluster
    idx = vq(FArray, centroids)

    plt.figure(figsize=(100, 50), dpi=100)
    plt.scatter(FArray[:, 0], FArray[:, 1], c=closest_centroid, s=100)
    show()
    return centroids,closest_centroid

def Affinity(points):
    FArray = np.asarray(points)
    af = AffinityPropagation(preference=-50).fit(FArray)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    n_clusters_ = len(cluster_centers_indices)

    plt.close('all')
    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        class_members = labels == k
        cluster_center = FArray[cluster_centers_indices[k]]
        plt.plot(FArray[class_members, 0], FArray[class_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
        for x in FArray[class_members]:
            plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()

def Spectral(cosineSimilarityMatrix):
    matrix=normalize(cosineSimilarityMatrix)
    algo=SpectralClustering(n_clusters=4,affinity='precomputed')
    return algo.fit_predict(cosineSimilarityMatrix)
