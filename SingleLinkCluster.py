import numpy as np


class Point:
    pass


class Cluster:
    pass


class Point:
    """
    Point object represents a vector of number values
    """
    vars = np.array()

    def __init__(self, vars: list(float | int)):
        self.vars = vars

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
    points = np.array()

    def __init__(self, points: list(Point)):
        self.points = points

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

    Step 4] repeat step 3 until there is only 1 point
    """

    clusters = []

    def __init__(self, clusters: list(Cluster)):
        self.clusters = clusters

    def plot(self):
        pass

    def calculate_distances(self):
        pass

    def closest_points(self):
        pass

    def cluster_points(self):
        pass

    def cluster(self):
        clustered = []

        self.plot()
        self.calculate_distances()

        while len(self.points) != 1:
            p1, p2 = self.closest_points()
            self.cluster_points(p1, p2)
            self.calculate_distances()

        return


def main():
    SLC


if __name__ == "__main__":
    main()
