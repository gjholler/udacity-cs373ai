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
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

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
    return_val = []
    open_list = []
    gValue = 0
    list_item = [gValue, init[0], init[1]]
    finished = 0
    open_list.append(list_item)
    grid[init[0]][init[1]] = 1
    
    while(not finished):
        
        # Is the goal in the list?
        for i in range(len(open_list)):
            if((open_list[i][1] == goal[0]) and (open_list[i][2] == goal[1])):
                return open_list[i]
                
        # The goal hasn't been found yet, so select a new cell
        # find the item in open_list with the lowest gValue
        list_item = min(open_list)
        
        # remove it from the list
        open_list.remove(list_item)

        print("take list item")
        print list_item
                  
        # Expand the node
        open_list.extend(expand_node(list_item))
        if(open_list == []):
            return_val = "fail"
            finished = 1
        else:
            print("new open list:")
            for i in range(len(open_list)):
                print("    " + repr(open_list[i]))
            print("----")
            

    return return_val # you should RETURN your result
    
        
def expand_node(listItem):
    new_gValue = listItem[0] + 1
    current_xy = [listItem[1],listItem[2]]
    return_list = []

    for i in range(len(delta)):
        new_x = current_xy[0] + delta[i][0]
        new_y = current_xy[1] + delta[i][1]

        # Make sure new_position is within the grid
        if((new_x >= 0) and (new_x < len(grid)) and (new_y >= 0) and (new_y < len(grid[0]))):
            
	    # Check to see if the new position has been checked
            if(grid[new_x][new_y] != 1):
            
                # Add it to the list
                return_list.append([new_gValue, new_x, new_y])
                grid[new_x][new_y] = 1

    return return_list

# Main
return_val = search()
#print("returned")
if(return_val):
    print return_val
else:
    print("fail")
