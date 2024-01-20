Closest Pair Algorithm Documentation
=

Introduction:
-
The provided Python 3 code implements an algorithm which finds two points with the smallest Euclidean distance among a set of points in a two-dimensional plane. The algorithm utilizes a divide-and-conquer strategy to efficiently solve the problem.


Classes:
-

- Point:
  + Represents a point in the 2D plane with attributes x and y.
  + Used to store coordinates of points.

Functions:
-

- CompareX(a,b):
  + Custom comparison function for sorting points based on the x-coordinate.
  + Used in sorting the points array.


- CompareY(a,b):
  + Custom comparison function for sorting points based on the y-coordinate.
  + Used in sorting the strip creation step.
  

- dist(p1,p2):
  + Calculates the Euclidean distance between two points.
  

- min_distances(x,y):
  + Returns the minimum value of two values.

  
- sortByX(points):
  + Sorts a list of points based on the x-coordinate.

  
- draw_points(pane, points, lines=None, split_point=None):
  + Visualize points on an image using OpenCV.
  + Optionally draws lines and a split point for visualization purposes.


- findClosest(points, n, pane=None):
  + Main function to find the closest pair of points using divide-and-conquer approach.
  + Recursively divides the points into smaller subsets until the base case is reached.
  + Merges the results from left and right halves and considers points in a "strip" around the middle.


- closestPair(points):
  + Wrapper function that initializes the soring and finding processes.
  + Returns the closest pair of points.


- generate_random_points(num_points):
  + Generates a list of Point instances with random coordinates within a specified range.

Usage 
-
1. Initializiation:
   + The script initializes a set of random points and displays them on a window using OpenCV.


2. Algorithm Execution:
   + The closest pair algorithm is applied to find the two closest points among the generated set.


3. Visualization:
   + The script visualizes the random points, the split point during the algorithm execution and the final closest pair in an animated manner.


4. Output:
   + Prints the coordinates of the randomly generated points and the coordinates of the closest pair.


Execution
-

1. Run the script:
   + Execute the script to generate random points, visualize the algorithm steps, and print the results.


2. Close window:
   + Close the OpenCV window to end the script.

Dependencies
-

Ensure that the required libraries (numpy, cv2, math and random) are installed before running the script.

Example
-
Output:

Random Points: [(x1, y1), (x2, y2), ..., (xn, yn)]

Points: (closest_x1, closest_y1) and (closest_x2, closest_y2)