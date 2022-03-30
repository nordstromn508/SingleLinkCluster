"""
main.py
    main thread of execution

    @author Nicholas Nordstrom
"""
from SingleLinkCluster import Point, Cluster, SLC


def main():
    # Test Point object Constructor
    p1 = Point([1, 0], 'p1')
    p2 = Point([1, 1], 'p2')
    p3 = Point([1, 3], 'p3')
    p4 = Point([1, 6], 'p4')
    p5 = Point([1, 10], 'p5')
    p6 = Point([1, 15], 'p6')

    # Test Point Object Operations
    # print(p1)
    # print(p2)
    # print('Distance between p1 and p2:', p1.dist(p2))

    # Test Cluster Object Constructor
    # c1 = Cluster([p1, p2], 'c1')
    # c2 = Cluster([p3, p4], 'c2')

    # Test Cluster Object Operations
    # print(c1)
    # print(c2)
    # print(c1.dist(c2))
    # c1.consume(c2)
    # print(c1)

    model = SLC()
    c0, c1, d = model.fit_predict([p1, p2, p3, p4, p5, p6])

    print('\nResults:')
    for i in range(len(c0)):
        print("Cluster " + c0[i] + " Consumed Cluster " + c1[i] + " Which Had A Distance Of " + str(d[i]))


if __name__ == '__main__':
    main()
