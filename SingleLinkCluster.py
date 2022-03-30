"""
SingleLinkCluster.py
    OOP implementation of single link cluster algorithm

    @author Nicholas Nordstrom
"""
import numpy as np
class Point: pass
class Cluster: pass


class Point:
    """
    Point object represents a vector of number values
    """

    def __init__(self, new_vars, name: str = None):
        """
        initalize new point object consisting of a vector of int or float values
        :param new_vars: vector to store in point object
        """
        self.vars = np.array(new_vars)
        self.name = name

    def __str__(self):
        """
        cast point object to a string
        :return:
        """
        return self.name + ':' + str(self.vars)

    def dist(self, p2: Point):
        """
        Calculate and return the distance between two points
        :param p2: second point
        :return: euclidean distance between self and the second point
        """
        return np.linalg.norm(self.vars - p2.vars)


class Cluster:
    """
    Cluster object represents a group of 0 or more points
    """

    def __init__(self, points, name: str = None):
        """
        initialize a cluster object constsing of 0 or more point objects
        :param points: point objects to store into cluster
        """
        self.points = points
        self.name = name

    def __str__(self):
        """
        convert cluster object to a neat looking description
        :return: string representation
        """
        return self.name + ':{' + ', '.join([str(p) for p in self.points]) + '}'

    def get_dists(self, c2: Cluster):
        """
        Calculate and return the minimum distance between any point in self and any point in the second cluster
        :param c2: second cluster
        :return: list of euclidean distances between self and the other cluster
        """
        dists = [len(self.points)*len(c2.points)]
        idx = 0
        for p1 in self.points:
            for p2 in c2.points:
                dists[idx] = p1.dist(p2)
                idx += 1
        return dists

    def dist(self, c2: Cluster):
        """
        Calculate and return the minimum distance between any point in self and any point in the second cluster
        :param c2: second cluster
        :return: minimum euclidean distance between self and the other cluster
        """
        n = len(self.points)
        m = len(c2.points)
        dists = np.empty((n*m))
        mask = np.empty((n*m, 2))

        idx = 0
        for i in range(n):
            for j in range(m):
                dists[idx] = self.points[i].dist(c2.points[j])
                mask[idx] = [i, j]
                idx += 1

        return np.min(dists)

    def consume(self, c2: Cluster):
        """
        Combine two clusters into one.
        :param c2: second cluster
        :return: None
        """
        self.name += ', ' + c2.name
        for p in c2.points:
            self.points.append(p)
        return None


class SLC:
    """
    Step 1] plot points

    Step 2] calculate distance between points

    Step 3] Identify two closest points and cluster them
            recompute distance matrix

    Step 4] repeat step 3 until there is only 1 cluster
    """
    def __init__(self):
        self.clusters = None

    def calculate_distances(self):
        """
        formula for number of comparisons needed for calculating all distances
            y = (x-1) * (x/2)
        Optimized: loop from n^2 runtime to (n/2) * (n-1)
        Optimized: cluster idexing using a mask
        :return: list of distances
        """
        l = len(self.clusters)
        dists = np.empty(int((l/2)*(l-1)))
        mask = np.empty((int((l/2)*(l-1)), 2))

        idx = 0
        for i in range(l-1):
            for j in range(i+1, l):
                dists[idx] = self.clusters[i].dist(self.clusters[j])
                mask[idx] = [i, j]
                idx += 1

        return dists, mask

    def closest_points(self):
        """
        Obtain the closest two points (or clusters)
        Optimized: Cluster Indexing using a mask
        TODO: Optimize function runtime so that calculate_distances is not called every time
        :return: indexes of the two closest points
        """
        dists, mask = self.calculate_distances()
        idx = np.argmin(dists)
        c0_idx, c1_idx = mask[idx]
        return int(c0_idx), int(c1_idx), dists[idx]

    def cluster_points(self, c0_idx: int, c1_idx: int):
        """
        Given two different cluster indexes, combine them into one cluster and resolve old references
        :param c0_idx: index value for cluster 0
        :param c1_idx: index value for cluster 1
        :return: None
        """
        self.clusters[c0_idx].consume(self.clusters[c1_idx])
        mask = np.ones_like(self.clusters, dtype=bool)
        mask[c1_idx] = 0
        self.clusters = self.clusters[mask]

    def fit_predict(self, points):

        self.clusters = np.array([c for c in list(map(Cluster, [[p] for p in points], ['c' + str(i) for i in range(len(points))]))])
        consumption_c0 = ['']*(len(self.clusters)-1)
        consumption_c1 = ['']*(len(self.clusters)-1)
        consumption_dist = np.empty((len(self.clusters) - 1))

        idx = 0
        while len(self.clusters) != 1:
            c0_idx, c1_idx, dist = self.closest_points()

            consumption_c0[idx] = self.clusters[c0_idx].name
            consumption_c1[idx] = self.clusters[c1_idx].name
            consumption_dist[idx] = dist
            self.cluster_points(c0_idx, c1_idx)
            idx += 1

        return consumption_c0, consumption_c1, consumption_dist
