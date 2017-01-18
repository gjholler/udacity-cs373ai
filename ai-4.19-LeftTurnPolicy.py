#!/usr/bin/python
from time import time
# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
#init = [2, 4, 2] # first 2 elements are coordinates, third is direction
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']



# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():
    # value takes the form [theta,x,y]
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for o in range(len(forward)):      # car can be in 1 of 4 orientations
                    if((goal[0] == x) and (goal[1] == y)):
                        value[o][x][y] = 0
                    elif(grid[x][y] == 0):
                        # calculate the cost of each action for each orientation
                        #for a in range(len(action_name)):
                        for a in range(3):

                            o2 = (o + action[a]) % len(forward)
                            x2 = x + forward[o2][0] 
                            y2 = y + forward[o2][1]

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[o2][x2][y2] + cost[a]

                                if(v2 < value[o][x][y]):
                                    change = True
                                    value[o][x][y] = v2
                                    #value[o][x][y] = v2

    finished = False
    x = init[0]
    y = init[1]
    o = init[2]

    while(not finished):
        if((goal[0] == x) and (goal[1] == y)):
            policy2D[x][y] = '*'
            finished = True
        else:
#            print("position is [" + repr(x) + "][" + repr(y) + "]. Orientation is " + repr(o))
            min = 999
            best_action = 0
            for a in range(len(action)):
                index = (o + action[a]) % len(forward)
                ax = x + forward[index][0]
                ay = y + forward[index][1]
                #print(repr(action_name[a]) + " turn costs " + repr(value[o][ax][ay]))
                if ax >= 0 and ax < len(grid) and ay >= 0 and ay < len(grid[0]):
                    current_value = value[o][ax][ay] 
                    if(current_value < min):
                        min = current_value
                        best_action = a
#            print(repr(action_name[best_action]) + " is currently the best turn")
            policy2D[x][y] = action_name[best_action]
            index = (o + action[best_action]) % len(forward)
            x += forward[index][0]
            y += forward[index][1]
            o = (o + action[best_action]) % len(forward)

            #print x
            #print y
            #print o

    return policy2D # Make sure your function returns the expected grid.

def optimum_policy2D_sebastian():
    # value takes the form [theta,x,y]
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    #### NEW
    policy = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(len(forward)):      # car can be in 1 of 4 orientations
                    if((goal[0] == x) and (goal[1] == y)):
                        if value[orientation][x][y] > 0:
                            change = True
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'                    ##### NEW
                    elif(grid[x][y] == 0):
                        # calculate the cost of each action for each orientation
                        for a in range(len(action)):
                            o2 = (orientation + action[a]) % len(forward)
                            x2 = x + forward[o2][0] 
                            y2 = y + forward[o2][1]

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[o2][x2][y2] + cost[a]

                                if(v2 < value[orientation][x][y]):
                                    change = True
                                    value[orientation][x][y] = v2
                                    policy[orientation][x][y] = action_name[a]    ##### NEW

    finished = False
    x = init[0]
    y = init[1]
    orientation = init[2]

    #### THE FOLLOWING IS NEW
    policy2D[x][y] = policy[orientation][x][y]
    while policy[orientation][x][y] != '*':
        if policy[orientation][x][y] == '#':
            o2 = orientation
        elif policy[orientation][x][y] == 'R':
            o2 = (orientation - 1) % 4
        elif policy[orientation][x][y] == 'L':
            o2 = (orientation + 1) % 4
        x = x + forward[o2][0]
        y = y + forward[o2][1]
        orientation = o2
        policy2D[x][y] = policy[orientation][x][y]

    return policy2D # Make sure your function returns the expected grid.


print("----- INITIAL POSITION -----")
print("position is [" + repr(init[0]) + "][" + repr(init[1]) + "]. Orientation is " + repr(init[2]))
print("----- GRID -----")
for i in range(len(grid)):
    print grid[i]
print("")
print("---------------------")
print("----- MY CODE -----")

t0 = time()
blah = optimum_policy2D()
t1 = time()
my_time = t1-t0
print("----- PATH -----")
for i in range(len(blah)):
    print blah[i]
print("Execution time: " + repr(my_time) + " seconds")


print("")
print("----------------------------")
print("----- SEBASTIAN'S CODE -----")

t0 = time()
blah = optimum_policy2D_sebastian()
t1 = time()
seb_time = t1-t0
print("----- PATH -----")
for i in range(len(blah)):
    print blah[i]
print("Sebastian's took : " + repr(seb_time) + " seconds")

if(my_time < seb_time):
    print("Mine ran " + repr ((seb_time - my_time) / seb_time * 100) + "% faster")
else:
    print("Mine ran slower")







