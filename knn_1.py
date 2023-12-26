# You're part of a team creating a statistical analysis library for Python. You're tasked with the nearest neighbor function
# For the sake of the problem, you can assume the input sizes won't be too large
# But your function will accept 2 inputs, a point A, and a list of other points B[]

# Your function should return the point C in the list B[] that is closest in euclidean distance to the given point A
# For example, here is one sample input
# Point A (0,0)
# B[(-1,-1),
# (3,4),
# (1,2),
# (5,6)]
# Your function should find that the first point, (-1,-1) is the closest.
# You can assume that each dimension will be an integer, and not decimal/float 
# However, the catch is that the points can be in many multiple dimensions
# So you can have a point as an x y coordinate like in the example
# Or x y z (0,0,0)
# Or in 5 dimensions (0,0,0,0,0)
# Etc
# You can assume that if the given point A has n dimensions, then all points in B[] will have the same number of dimensions as point A

# the Euclidean distance formula is distance = y2 - y1 / x2 - x1 
    # does this continue to work for other dimensions?

    # that is wrong, that is the slope formula
    
####LOOKED THIS UP####
# the Euclidean distance formula is sqrt( (x2-x1)^2 + (y2-y1)^2 )
# for N number dimensions, the formula is sqrt((Bi)^2 - (Ai)^2), where B and A are sets that represent each point
# List = [(1,5,3),(1,5,4),(1,5,5),(1,5,6)]
# EX A = (0,0,0) B = (1,5,3)
# Distance = sqrt((1-0)^2 + (5-0)^2 + (3-0)^2)
# => (1,5,3)

# EX A = (0,0,0,0,0) B = (1,5,3,0,0)
# Distance = sqrt((1-0)^2 + (5-0)^2 + (3-0)^2)


def calculate_n_dimensional_euclidean_distance(pointA: tuple, pointB: tuple) -> int:
    runningSum = 0
    for i in range(len(pointA)):
        runningSum += (pointB[i] - pointA[i])**2
    return runningSum**0.5

def nearest_point_locator(pointA: tuple, array: list[tuple]) ->  tuple:
    min_distance = float('inf')
    smallest_point = ()
    for pointB in array:
        distance = calculate_n_dimensional_euclidean_distance(pointA,pointB)
        if distance < min_distance:
            min_distance = distance
            smallest_point = pointB
    return smallest_point

print(nearest_point_locator((0,0,0), [(1,5,3),(1,5,4),(1,5,5),(1,5,6)]))
print(nearest_point_locator((1,1,2), [(1,5,3),(1,5,4),(1,5,5),(1,5,6)]))
print(nearest_point_locator((0,0,0,0,0), [(1,5,3,0,0),(1,5,4,0,0),(1,5,5,0,0),(1,5,6,0,0)]))