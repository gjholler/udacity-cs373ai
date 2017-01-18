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

# ANSWER
# [0.000,0.000]
# [0.029,0.971]
# [0.176,1.825]
# [1.029,1.978]
# [2.000,2,042]
# [2.971,2.272]
# [3.824,3.589]
# [3.971,3.245]
# [4.000,4.000]

# ------------------------------------------------
# smooth coordinates
#
#def smooth_instructorAnswer(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):
def smooth_instructorAnswer(path, weight_data = 0., weight_smooth = 0.1, tolerance = 0.000001):
    # Make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]

    change = tolerance
    while (change >= tolerance):
        change = 0.0
        for i in range(1,len(path)-1):
            for j in range(len(path[0])):
                aux = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j])
                newpath[i][j] += weight_smooth * (newpath[i-1][j] + newpath[i+1][j] - (2.0 * newpath[i][j]))
                change += abs(aux - newpath[i][j])
    return newpath # Leave this line for the grader!









def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]

    num_loops = 1
    #### ENTER CODE BELOW THIS LINE ###
    finished = False
    smooth_term = [0,0]
    temp = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    tolerance = tolerance ** 2
 
    while(not finished):
        finished = True
        delta = 0
        for x in range(1,len(path)-1):
            for y in range(len(path[0])):
                temp[x][y] = newpath[x][y]
                temp[x][y] += weight_data * (newpath[x][y] - path[x][y])
                temp[x][y] += weight_smooth * ((2*newpath[x][y]) - newpath[x+1][y] - newpath[x-1][y])
                delta += (path[x][y] - temp[x][y]) ** 2              
                print delta
                #delta += 
        for x in range(1,len(path)-1):
            for y in range(len(path[0])):
                newpath[x][y] -= weight_data*temp[x][y]        

        if(delta > tolerance):
            finished = False
#            if((abs(yi[0] - newpath[i][0]) > tolerance) and (abs(yi[1] - newpath[i][1]) > tolerance)):
#                print("x difference is " + repr(abs(yix - newpath[i][0])))
#                print("y difference is " + repr(abs(yiy - newpath[i][1])))

#                finished = False
            # Update newpath 
#            newpath[i][0] = yi[0]
#            newpath[i][1] = yi[1]
        num_loops += 1

    print("num_loops: " + repr(num_loops))
    return newpath # Leave this line for the grader!


def smooth_works(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]

    num_loops = 1
    #### ENTER CODE BELOW THIS LINE ###
    finished = False
    smooth_term = [0,0]
     
    while(not finished):
        finished = True
        for i in range(1,len(path)-1):
            xix = path[i][0]
            xiy = path[i][1]
            yix = newpath[i][0]
            yiy = newpath[i][1]
            yim1 = newpath[i-1]
            yip1 = newpath[i+1]

            # Add alpha
            #yix -= weight_data * (yix - xix)
            #yiy -= weight_data * (yiy - xiy)
            yix -= weight_data * (xix - yix)
            yiy -= weight_data * (xiy - yiy)
            #yi[0] += weight_data * (xix - yix)
            #yi[1] += weight_data * (xiy - yiy)

            # Smooth
            #yix += (weight_smooth) * ((2 * newpath[i][0]) - newpath[i+1][0] - newpath[i-1][0])
            #yiy += (weight_smooth) * ((2 * newpath[i][1]) - newpath[i+1][1] - newpath[i-1][1])
            yix += (weight_smooth) * (newpath[i+1][0] + newpath[i-1][0] - (2 * newpath[i][0]))
            yiy += (weight_smooth) * (newpath[i+1][1] + newpath[i-1][1] - (2 * newpath[i][1]))

            #smooth_term[0] = yip1[0] + yim1[0] - (2*yi[0])
            #smooth_term[1] = yip1[1] + yim1[1] - (2*yi[1])
            #yi[0] += weight_smooth * smooth_term[0]
            #yi[1] += weight_smooth * smooth_term[1]
          
            print("y[i]: " + repr(yix) + "," + repr(yiy)+ ", newpath[i]: " + repr(newpath[i])) 
            #x_difference = yi[0] - newpath[i][0]
            #y_difference = yi[1] - newpath[i][1]
            #if(x_difference != 0 and y_difference != 0):
            #if(((yi[0] - newpath[i][0]) < tolerance) and ((yi[1] - newpath[i][1]) < tolerance)):
            if((abs(yix - newpath[i][0]) > (tolerance**2)) or (abs(yiy - newpath[i][1]) > (tolerance**2))):
                print("x difference is " + repr(abs(yix - newpath[i][0])))
                print("y difference is " + repr(abs(yiy - newpath[i][1])))

                finished = False
            # Update newpath 
            newpath[i][0] = yix
            newpath[i][1] = yiy
        num_loops += 1

    print("num_loops: " + repr(num_loops))
    return newpath # Leave this line for the grader!


# feel free to leave this and the following lines if you want to print.
t0 = time()
newpath = smooth_instructorAnswer(path)
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



def smooth_straightline(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]

    num_loops = 1
    #### ENTER CODE BELOW THIS LINE ###
    finished = False
    smooth_term = [0,0]
     
    while(not finished):
        finished = True
        for i in range(1,len(path)-1):
            xi = newpath[i]
            yi = xi
            yim1 = newpath[i-1%len(newpath)]
            yip1 = newpath[i+1%len(newpath)]

            #
            yi[0] += weight_data * (xi[0] - yi[0])
            yi[1] += weight_data * (xi[1] - yi[1])

            # Smooth
            smooth_term[0] = yip1[0] + yim1[0] - (2*yi[0])
            smooth_term[1] = yip1[1] + yim1[0] - (2*yi[1])
            if((smooth_term[0] > tolerance) or (smooth_term[1] > tolerance)):
                finished = False
            yi[0] += weight_smooth * smooth_term[0]
            yi[1] += weight_smooth * smooth_term[1]
           
            # Update newpath 
            newpath[i][0] = yi[0]
            newpath[i][1] = yi[1]
        num_loops += 1

    print("num_loops: " + repr(num_loops))
    return newpath # Leave this line for the grader!



