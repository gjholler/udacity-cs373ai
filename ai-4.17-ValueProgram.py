#!/usr/bin/python

# -----------
# User Instructions:
#
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1

########
# should output
########

#[12,11,99,7,6,5]
#[11,10,99,6,5,4]
#[10, 9,99,5,4,3]
#[ 9, 8, 7,6,99,2]
#[10, 9,99,99,99,1]
#[11,10,11,12,99,0]

# ----------------------------------------
# insert code below
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

            print("----- open before pop -----")
            print open
            next = min(open)
            open.remove(next)
            print("next: " + repr(next))
            print("open: " + repr(open))
            print("------------------------")
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





blah = compute_value()

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
