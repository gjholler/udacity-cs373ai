#!/usr/bin/python

#Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. NOTE: the 'v' should be 
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    # create a list of "search sets"
    # each row contains a search path
    # each element contains x,y,direction
    search_set = [[]]

    x = init[0]
    y = init[1]
    g = 0
    s = 0         # current search set

    open = [[g, x, y, s]]
    search_set[0].append([x,y,0])

    found = False  # flag that is set when search is complet
    resign = False # flag set if we can't find expand

    while not found and not resign:
        first_empty_cell_found = False

        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            s = next[3]
 
            if x == goal[0] and y == goal[1]:
                found = True
                expand = draw_map(expand, search_set[s])
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if(closed[x2][y2] == 0 and grid[x2][y2] == 0):
                            if(first_empty_cell_found == True):
                                s = add_new_search_path(search_set,s)
                            first_empty_cell_found = True
                            g2 = g + cost
                            open.append([g2, x2, y2, s])
                            closed[x2][y2] = 1
                            search_set[s].append([x,y,i])
    return_list = []
    for i in range(len(search_set[s])):
        temp = [search_set[s]
        return_list.append(search_set
    for i in range(len(expand)):
        print expand[i]
    return # make sure you return the shortest path.

def add_new_search_path(search_set, s):
    # appends a row to search_set, and copies row s to it (ignoring last element in row)
    # returns: row number s
    search_set.append(search_set[s][:-1])
    
    return (len(search_set) - 1)

def draw_map(m, goal_path):
    # m - matrix showing the optimal path to the goal
    # goal_path - list containing the search path
    return_map = [[' ' for row in range(len(m[0]))] for col in range(len(m))]

    for i in range(len(goal_path)):
        x = goal_path[i][0]
        y = goal_path[i][1]
        direction = goal_path[i][2]
        return_map[x][y] = delta_name[direction]

    # draw the goal
    return_map[goal[0]][goal[1]] = '*'     # sorta cheating...

    return return_map

search()
