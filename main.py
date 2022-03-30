"""
main.py
    main thread of execution

    @author Nicholas Nordstrom
"""
from SingleLinkCluster import Point, Cluster, SLC


def main():
    model = SLC()
    p1 = Point([1, 0], 'p1')
    print(p1)
    c1 = Cluster([p1], 'c1')
    print(c1)


if __name__ == '__main__':
    main()
