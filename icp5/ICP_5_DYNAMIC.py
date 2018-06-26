# numpy library importing
import numpy as np

# import matplotlib for plotting the graph(centroid, points etc)
import matplotlib.pyplot as plt

# random generation for initial centroid calculating
import random


def create_cluster(X, centroid_pts):
    cluster = {}
  # read about lambdas and np.linalg.form
  # https://stackoverflow.com/questions/32141856/is-norm-equivalent-to-euclidean-distance ,
  # here we are using order 1 to calculate normalized distance
    for x in X:
        value = min([(i[0],np.linalg.norm(x - centroid_pts[i[0]]))for i in enumerate(centroid_pts)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster

# Calculate new centroid
def calculate_new_center(cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu

# match the old and new centroids by comparing values
def matched(new_centroids, old_centroids):
    return (set([tuple(a)for a in new_centroids]) == set([tuple(a)for a in old_centroids]))

# Applying k means by passing the height, weight values
def Apply_Kmeans(X, K, N):
    # selecting random centroids from dataset and by number of clusters.
    old_centroids = np.random.randint(N, size = K)
    old_centroid_pts = np.array([X[i]for i in old_centroids])

    # old centroids which are generated randomly
    print("old :",old_centroids)
    print(old_centroid_pts)

    cluster_info = create_cluster(X, old_centroid_pts)

    print("Initial cluster information:")
    print(cluster_info)

    # new centroid values after calculation
    new_centroid_pts=calculate_new_center(cluster_info)
    print("new :", new_centroid_pts)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    plot_cluster(old_centroid_pts,cluster_info,itr)
    while not matched(new_centroid_pts, old_centroid_pts):
        itr = itr + 1
        old_centroid_pts = new_centroid_pts
        cluster_info = create_cluster(X,new_centroid_pts)
        plot_cluster(new_centroid_pts, cluster_info,itr)
        new_centroid_pts = calculate_new_center(cluster_info)

    print("Results after final iteration:")
    plot_cluster(new_centroid_pts, cluster_info, itr)
    return


def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()

# PLot graph by passing height, weight
def init_graph(N,height, width):
    X = np.array([(random.choice(height),random.choice(width))for i in range(N)])
    return X


def Simulate_Clusters():

    # this way we can dynamically pass the values of any size like 100 X 100 elements
    print("-----K means program ----")

    # No. of points to be present in each cluster
    N = int(input('Enter the number of points.......'))

    # No. of clusters we want to generate
    K = int(input('Enter the number of Clusters.......'))

   print('Now Enter the bounds for choosing uniform value....\n')
  p1 = int(input('Enter the lower bound for points.......'))
  p2 = int(input('Enter the upper bound for points.......'))
