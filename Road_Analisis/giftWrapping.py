from collections import namedtuple  
import matplotlib.pyplot as plt  
import random
from location_tools import *
from test_tools import *
from tools import *
from random import uniform

Point = namedtuple('Point', 'x y')

class ConvexHull(object):  
    _points = []
    _hull_points = []

    def __init__(self):
        pass

    def add(self, point):
        self._points.append(point)

    def _get_orientation(self, origin, p1, p2):
        
        difference = (
            ((p2.x - origin.x) * (p1.y - origin.y))
            - ((p1.x - origin.x) * (p2.y - origin.y))
        )

        return difference

    def compute_hull(self):
        
        points = self._points

        # get leftmost point
        start = points[0]
        min_x = start.x
        for p in points[1:]:
            if p.x < min_x:
                min_x = p.x
                start = p

        point = start
        self._hull_points.append(start)

        far_point = None
        while far_point is not start:

            # get the first point (initial max) to use to compare with others
            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                # ensure we aren't comparing to self or pivot point
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            self._hull_points.append(far_point)
            point = far_point

    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.compute_hull()

        return self._hull_points

    def display(self):
        # all points
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.plot(x, y, marker='D', linestyle='None')

        # hull points
        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]
        plt.plot(hx, hy)

        plt.title('Convex Hull')
        plt.show()

def giftWrappedBoardSize(georeferencesPath):  
    
    ch = ConvexHull()

    locs = loadLocations(georeferencesPath)

    for loc in locs:
        ch.add(Point(float(loc[0]), float(loc[1])))
        ch.add(Point(float(loc[2]), float(loc[3])))

    hull_points = ch.get_hull_points()

    lons = [abs(point[0]) for point in ch.get_hull_points()]
    lats = [abs(point[1]) for point in ch.get_hull_points()]

    maxLon = max(lons)
    minLon = min(lons)
    maxLat = max(lats)
    minLat = min(lats)
    
    point_1 = [minLon, maxLat]
    point_2 = [maxLon, maxLat]
    point_3 = [maxLon, minLat]
    point_4 = [minLon, minLat]

    print('Outer Points')
    print(point_1, point_2)
    print(point_4, point_3) 

    #plt.plot(minLon, maxLat, 'o')
    #plt.plot(maxLon, minLat, '-*')
    #plt.title('Outmosts')
    #plt.show()

    W = coordinatesToMeters(point_1, point_2)

    H = coordinatesToMeters(point_1, point_4)

    #ch.display()

    return H, W

def coordConvexHull(georeferencesPath):
    
    ch = ConvexHull()

    locs = loadLocations(georeferencesPath)

    for loc in locs:
        ch.add(Point(float(loc[0]), float(loc[1])))
        ch.add(Point(float(loc[2]), float(loc[3])))

    hull_points = ch.get_hull_points()

    lons = [abs(point[0]) for point in ch.get_hull_points()]
    lats = [abs(point[1]) for point in ch.get_hull_points()]

    maxLon = max(lons)
    minLon = min(lons)
    maxLat = max(lats)
    minLat = min(lats)
    
    point_1 = [minLon, maxLat]
    point_2 = [maxLon, maxLat]
    point_3 = [maxLon, minLat]
    point_4 = [minLon, minLat]

    print('Outer Points')
    print(point_1, point_2)
    print(point_4, point_3) 

    W = coordinatesToMeters(point_1, point_2)

    H = coordinatesToMeters(point_1, point_4)

    print(H, W)

    ch.display()

    plt.plot(minLon, maxLat, '-*')
    plt.plot(maxLon, minLat, '-*')
    plt.plot(minLon, minLat, 'o')
    plt.plot(maxLon, maxLat, 'o')
    plt.title('Outmosts')
    plt.show()

if __name__ == '__main__':  
    main()