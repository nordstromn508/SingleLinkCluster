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

    def __init__(self, new_vars: list(float | int)):
        """
        initalize new point object consisting of a vector of int or float values
        :param new_vars: vector to store in point object
        """
        self.vars = new_vars

    def dist(self, p2: Point):
        """
        Calculate and return the distance between two points
        :param p2: second point
        :return: euclidean distance between self and the second point
        """
        return np.linalg.norm(self.vars, p2.vars)


class Cluster:
    """
    Cluster object represents a group of 0 or more points
    """

    def __init__(self, points: list(Point)):
        """
        initialize a cluster object constsing of 0 or more point objects
        :param points: point objects to store into cluster
        """
        self.points = points
        self.dists = None

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
        min = self.points[0].dist(c2.points[0])
        for p1 in self.points:
            for p2 in c2.points:
                min = np.min(min, p1.dist(p2))
        return min

    def consume(self, c2: Cluster):
        """
        Combine two clusters into one.
        :param c2: second cluster
        :return: None
        """
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
        calculate
        :return: list of index
        """
        dists = np.empty(len(self.clusters)-1)
        for c1 in self.clusters:
            idx = 0
            for c2 in self.clusters:
                if c1 is not c2:
                    dists[idx] = c1.dist(c2)
                idx += 1
            c1.dists = dists

        pass

    def closest_points(self):
        dists = self.calculate_distances()

        np.argmin(dists)
        dists[]
        return c1_idx, c2_idx

    def cluster_points(self, c1_idx, c2_idx):
        pass

    def fit(self, points):
        self.clusters = [c for c in [Cluster([p]) for p in points]]

        while len(self.clusters) != 1:
            self.cluster_points(self.closest_points())

    def predict(self):
        pass

def main():
    SLC


if __name__ == "__main__":
    main()
