import cv2
import math
import numpy as np
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def compareX(a, b):
    if a.x != b.x:
        return a.x - b.x
    else:
        return a.y - b.y  # compare by y if x is the same

def compareY(a, b):
    if a.y != b.y:
        return a.y - b.y
    else:
        return a.x - b.x  # compare by x if y is the same

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)  # distance between two points

def min_distances(x, y):
    return x if x < y else y  # returns minimum of two values

def sortByX(points):
    return sorted(points, key=lambda p: p.x)  # sorting the points based on the x coordinate

def draw_points(pane, points, lines=None, split_point=None):
    pane[:] = (255, 255, 255)
    radius = 5

    center_x, center_y = pane.shape[1] // 2, pane.shape[0] // 2

    for point in points:
        shifted_x, shifted_y = center_x + point.x, center_y + point.y
        cv2.circle(pane, (shifted_x, shifted_y), radius, (0, 0, 0), -1)

    if lines is not None:
        for line in lines:
            cv2.line(pane, (line[0].x + center_x, line[0].y + center_y),
                     (line[1].x + center_x, line[1].y + center_y), (0, 0, 255), 2)

    if split_point is not None:
        cv2.line(pane, (split_point.x + center_x, 0), (split_point.x + center_x, pane.shape[0]), (0, 255, 0), 2)

    cv2.imshow("Closest Pair", pane)
    cv2.waitKey(1000)


def findClosest(points, n, pane=None):
    if n < 4:
        min_dist = float('inf')
        min_pair = None
        for i in range(n):
            for j in range(i + 1, n):
                current_dist = dist(points[i], points[j])
                if current_dist < min_dist:
                    min_dist = current_dist
                    min_pair = (points[i], points[j])

                    if pane is not None:
                        draw_points(pane, points, lines=[min_pair])

        return min_dist, min_pair

    # divide

    mid = n // 2
    midPoint = points[mid]

    left_points = points[:mid]  # recursive calls for the left and right halves
    right_points = points[mid:]

    # Draw the split point
    if pane is not None:
        draw_points(pane, points, split_point=midPoint)

    # conquer

    left_closest, left_pair = findClosest(left_points, mid, pane)
    right_closest, right_pair = findClosest(right_points, n - mid, pane)

    # to combine: calculate the minimum distance delta between the closest pairs from left and right halves

    # merge

    delta = min_distances(left_closest, right_closest)

    # creates a strip of points within delta distance of the dividing line (midpoint)

    strip = [point for point in points if abs(point.x - midPoint.x) < delta]
    strip.sort(key=lambda point: point.y)   # strip is sorted based on y coordinate

    strip_closest = delta
    strip_pair = None
    for i in range(len(strip)):     # iterate through the strip to find points closer than delta based on y coordinate
        for j in range(i + 1, len(strip)):
            if (strip[j].y - strip[i].y) < strip_closest:
                current_dist = dist(strip[i], strip[j])
                if current_dist < strip_closest:
                    strip_closest = current_dist
                    strip_pair = (strip[i], strip[j])

                    if pane is not None:
                        draw_points(pane, points, lines=[strip_pair])

    # function returns the closest distance among the following:

    if strip_pair is not None:
        return strip_closest, strip_pair  # closest pair in the strip
    elif left_closest < right_closest:
        return left_closest, left_pair   # closest pair in the left half
    else:
        return right_closest, right_pair  # closest pair in the right half

def closestPair(points):
    sorted_points = sortByX(points)
    _, closest_pair = findClosest(sorted_points, len(sorted_points), pane=np.zeros((800, 800, 3), dtype=np.uint8))
    draw_points(np.zeros((800, 800, 3), dtype=np.uint8), points, lines=[closest_pair])
    return closest_pair

def generate_random_points(num_points):
    return [Point(random.randint(1, 100), random.randint(1, 100)) for _ in range(num_points)]

if __name__ == "__main__":
    # generate 10 random points
    random_points = generate_random_points(10)

    # create a larger window to center the points
    draw_points(np.zeros((1200, 1200, 3), dtype=np.uint8), random_points)

    # find the closest pair among the random points
    result_pair = closestPair(random_points)

    print(f"Random Points: {[(point.x, point.y) for point in random_points]}")
    print(f"Points: ({result_pair[0].x}, {result_pair[0].y}) and ({result_pair[1].x}, {result_pair[1].y})")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
