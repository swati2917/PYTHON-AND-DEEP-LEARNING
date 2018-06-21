import numpy as np
import matplotlib.pyplot as plt

# calculating centroids on shirt sizes
def Clustering(points, Centroid1, Centroid2, Centroid3):
    print("T-Shirt size clustering")
    print("T-shirtsizes =", points)
    print("First centroid =", Centroid1)
    print("Second centroid =", Centroid2)
    print("Third centroid =", Centroid3)

    prevC1 = None
    prevC2 = None
    prevC3 = None

    C1 = Centroid1
    C2 = Centroid2
    C3 = Centroid3

    i = 0
    while C1 != prevC1 or C2 != prevC2 or C3 != prevC3:
        i += 1
        print("\nIteration", i, ":")
        cluster1 = []
        cluster2 = []
        cluster3 = []
        for x in points:
            distance1 = abs(C1 - x)
            distance2 = abs(C2 - x)
            distance3 = abs(C3 - x)
            if distance1 < distance2 and distance1<distance3:
                cluster1.append(x)
                Distance1 = "(%.1f)" % distance1
                Distance2 = "%.1f" % distance2
                Distance3 = "%.1f" % distance3
            elif distance2 < distance3 and distance2<distance1:
                cluster2.append(x)
                Distance1 = "(%.1f)" % distance1
                Distance2 = "%.1f" % distance2
                Distance3 = "%.1f" % distance3
            else:
                cluster3.append(x)
                Distance1 = "%.1f" % distance1
                Distance2 = "(%.1f)" % distance2
                Distance3 = "%.1f" % distance3
        print("Cluster Centroids:")
        print("cluster 1 =", cluster1)
        print("cluster 2 =", cluster2)
        print("cluster 3 =", cluster3)
        print("\nCalculating new centroids:")
        prevC1 = C1
        prevC2 = C2
        prevC3 = C3
        C1 = np.mean(cluster1)
        C2 = np.mean(cluster2)
        C3 = np.mean(cluster3)
        print("centroid 1 =", C1)
        print("centroid 2 =" ,C2)
        print("centroid 3 = ",C3)

    plt.scatter(points, weight)
    plt.plot(C1, 30, color='red', marker='x') # assuming mean of weight is 30
    plt.plot(C2, 40, color='red', marker='x') # assuming mean of weight is 40
    plt.plot(C3, 50, color='red', marker='x') # assuming mean of weight is 50
    plt.title("T-Shirt Clustering")
    plt.show()
    print("As the centroids have not changed no more iteration to be done!")


def Mean(datalist):
    if len(datalist) == 0:
        return ""
    else:
        s = "(" + str(datalist[0])
        for i in range(1, len(datalist)):
            s += " + " + str(datalist[i])
        s += ") / " + str(len(datalist))
        return s

# initialising shirt size arrays
points = np.array([18, 19, 20, 21, 22, 23, 28, 29, 30, 32, 33, 41, 37, 38, 39, 42])
# initialising weights arrays
weight = np.array([32, 28, 34, 26, 22, 38, 42, 40, 44, 36, 38, 50, 50, 48, 52, 50])
# plot of data
plt.title("Initial data")
plt.scatter(points, weight)
plt.show()
Centroid1 = 20
Centroid2 = 30
Centroid3 = 40
Clustering(points, Centroid1, Centroid2, Centroid3)