#!/usr/bin/python

# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth)
# and returns a smooth path.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the previous video:
#
# If your function isn't submitting it is possible that the
# runtime is too long. Try sacrificing accuracy for speed.
# -----------


from math import *
from time import time
from plotting import *

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1):

    # Make a deep copy of path into newpath
    rows = len(path)
    cols = len(path[0])
    newpath = [[path[row][col] for col in range(cols)] for row in range(rows)]

    tolerance = 0.000001 ** 2
    alpha = 0.8 # adjustable parameter for gradient descent
    change = tolerance
    dell = [[0 for col in range(cols)] for row in range(rows)] 
    while change >= tolerance : 
        change = 0
        for i in range(1, rows - 1) :
            for j in range(cols) :
                dell[i][j] = weight_data * (newpath[i][j] - path[i][j]) 
                dell[i][j] += weight_smooth * (2 * newpath[i][j] - newpath[i - 1][j] - newpath[i + 1][j])
                change += (alpha * dell[i][j]) ** 2
        for i in range(1, rows - 1):
            for j in range(cols):
                newpath[i][j] -= alpha * dell[i][j]

    return newpath # Leave this line for the grader!

t0 = time()
newpath = smooth(path)
t1 = time()
print(repr(t1-t0) + " seconds")
plotx = []
ploty = []
# thank you - EnTerr - for posting this on our discussion forum
for i in range(len(path)):
    plotx.append(newpath[i][0])
    ploty.append(newpath[i][1])
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'
scatterplot(plotx,ploty)

