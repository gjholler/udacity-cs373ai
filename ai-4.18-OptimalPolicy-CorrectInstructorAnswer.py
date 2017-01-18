#!/usr/bin/python

# -----------
# User Instructions:
#
# Create a function optimum_policy() that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell.
# 
# un-navigable cells must contain an empty string
# WITH a space, as shown in the previous video.
# Don't forget to mark the goal with a '*'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1



####
# calculate the heuristic
# loop through the matrix
#   at each cell, look at the 4 neighbors
#   whichever is the smallest, put delta_name[i] in the policy matrix
####



# ----------------------------------------
# my code below
# ----------------------------------------

def optimum_policy():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0

                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost_step

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2

    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if(value[x][y] == 99):
                continue
            current_value = value[x][y]
            for a in range(len(delta)):
                x2 = x + delta[a][0]
                y2 = y + delta[a][1]
                if (x2 >= 0) and (x2 < len(grid)) and (y2 >= 0) and (y2 < len(grid[0])) and (value[x2][y2] != 99):
                    neighbor_value = value[x2][y2]
                    if(neighbor_value < current_value):
                        policy[x][y] = delta_name[a] 
    policy[x][y] = '*' 
    return policy # Make sure your function returns the expected grid.

# ----------------------------------------
# my code above
# ----------------------------------------

# ----------------------------------------
# Sebastian's code below
# ----------------------------------------

def sebastians_optimum_policy():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    i = 1
    while change:
        print("While loop. i is " + repr(i))
        i += 1
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*' 
                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost_step

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                policy[x][y] = delta_name[a]




    return policy # Make sure your function returns the expected grid.

# ----------------------------------------
# Sebastian's code above
# ----------------------------------------


print("----- my optimum_policy -----")
blah = optimum_policy()
for i in range(len(blah)):
    print blah[i]

print("----- Sebastian's optimum_policy -----")
blah = sebastians_optimum_policy()
for i in range(len(blah)):
    print blah[i]
