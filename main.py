"""
main.py
    main thread of execution

    @author Nicholas Nordstrom
"""
from SingleLinkCluster import Point, Cluster, SLC


def main():
    model = SLC()
    p1 = Point([1, 0], 'p1')
    print(str(p1))

if __name__ == '__main__':
    main()
