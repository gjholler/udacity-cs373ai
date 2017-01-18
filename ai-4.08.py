#!/usr/bin/python

# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1



def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    path = 0
    open_list = []
    list_item = [0, init[0], init[1]]

    while((list_item[0] != goal[0]) and (list_item[1] != goal[1])):
        print("take list item")
        print list_item
    
        open_list = get_valid_moves([0,0,0])
        print("new open list:")
        for i in range(len(open_list)):
            print("    " + repr(open_list[i]))
        print("----")

    return path # you should RETURN your result



def get_valid_moves(current_pos):
    current_gValue = current_pos[0]
    current_xy = [current_pos[1], current_pos[2]]
    return_list = []

    for i in range(len(delta)):
        new_x = current_xy[0] + delta[i][0]
        new_y = current_xy[1] + delta[i][1]

        # Make sure new_position is within the grid
        if((new_x < 0)
           or (new_x == len(grid[0]))
           or (new_y < 0)
           or (new_y == len(grid))):
            continue

        # Check to see if the new position is occupied
        if(grid[new_x][new_y] == 1):
            continue

        # Add it to the list and mark grid position as checked
        return_list.append([current_gValue + 1, new_x, new_y])
        grid[new_x][new_y] = 1

    return return_list

# Main
path = search()

if(path):
    print("###### Search successful")
else:
    print("fail")
