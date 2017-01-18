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
# modify code below
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
# modify code above
# ----------------------------------------



def compute_value():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

    x = goal[0]
    y = goal[1]
    g = 0
    value[x][y] = g
    open = [[g,x,y]]

    finished = False

    while not finished:
        if(len(open) == 0):
            finished = True
        else:

#            print("----- open before pop -----")
#            print open
            next = min(open)
            open.remove(next)
#            print("next: " + repr(next))
#            print("open: " + repr(open))
#            print("------------------------")
            g = next[0]
            x = next[1]
            y = next[2]
            closed[x][y] = 1

            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                g2 = g + 1
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    if (grid[x2][y2] == 1):
                        value[x2][y2] = 99
                    elif(closed[x2][y2] != 1):
                        open.append([g2,x2,y2])
                        closed[x2][y2] = 1
                        value[x2][y2] = g2

   

    return value #make sure your function returns a grid of values as demonstrated in the previous video.

#print("----- compute_value -----")
#blah = compute_value()
#for i in range(len(blah)):
#    print blah[i]


print("----- optimum_policy -----")
blah = optimum_policy()
for i in range(len(blah)):
    print blah[i]



def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]


    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[x][y]

    open = [[f, g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    count = 0
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[2]
            y = next[3]
            g = next[1]
            f = g + heuristic[x][y]
            expand[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            f2 = g2 + heuristic[x2][y2]
                            open.append([f2, g2, x2, y2])
                            closed[x2][y2] = 1
    for i in range(len(expand)):
        print expand[i]
    return expand #Leave this line for grading purposes!

# ----------------------------------------
# to here
# ----------------------------------------

#search()
