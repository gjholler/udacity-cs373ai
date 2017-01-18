#!/usr/bin/python

# -------------------
# Background Information
#
# In this problem, you will build a planner that helps a robot
# find the shortest way in a warehouse filled with boxes
# that he has to pick up and deliver to a drop zone.
#For example:
#
#warehouse = [[ 1, 2, 3],
#             [ 0, 0, 0],
#             [ 0, 0, 0]]
#dropzone = [2,0] 
#todo = [2, 1]
# Robot starts at the dropzone.
# Dropzone can be in any free corner of the warehouse map.
# todo is a list of boxes to be picked up and delivered to dropzone. 
# Robot can move diagonally, but the cost of diagonal move is 1.5 
# Cost of moving one step horizontally or vertically is 1.0
# If the dropzone is at [2, 0], the cost to deliver box number 2
# would be 5.

# To pick up a box, robot has to move in the same cell with the box.
# When a robot picks up a box, that cell becomes passable (marked 0)
# Robot can pick up only one box at a time and once picked up 
# he has to return it to the dropzone by moving on to the cell.
# Once the robot has stepped on the dropzone, his box is taken away
# and he is free to continue with his todo list.
# Tasks must be executed in the order that they are given in the todo.
# You may assume that in all warehouse maps all boxes are
# reachable from beginning (robot is not boxed in).

# -------------------
# User Instructions
#
# Design a planner (any kind you like, so long as it works).
# This planner should be a function named plan() that takes
# as input three parameters: warehouse, dropzone and todo. 
# See parameter info below.
#
# Your function should RETURN the final, accumulated cost to do
# all tasks in the todo list in the given order and this cost
# must which should match with our answer).
# You may include print statements to show the optimum path,
# but that will have no effect on grading.
#
# Your solution must work for a variety of warehouse layouts and
# any length of todo list.
# Add your code at line 76.
# 
# --------------------
# Parameter Info
#
# warehouse - a grid of values. where 0 means that the cell is passable,
# and a number between 1 and 99 shows where the boxes are.
# dropzone - determines robots start location and place to return boxes 
# todo - list of tasks, containing box numbers that have to be picked up
#
# --------------------
# Testing
#
# You may use our test function below, solution_check
# to test your code for a variety of input parameters. 

warehouse = [[ 1, 2, 3],
             [ 0, 0, 0],
             [ 0, 0, 0]]
dropzone = [2,0] 
todo = [2, 1]

# ------------------------------------------
# plan - Returns cost to take all boxes in the todo list to dropzone
#
# ----------------------------------------
# modify code below
# ----------------------------------------
def plan(warehouse, dropzone, todo):

    box_locations = {}
    cost = 0
    diagonal_cost = 1.5
    straight_cost = 1.0

    delta = [[-1, -1, 1.5],   # North-West
             [-1,  0, 1.0],   # North
             [-1,  1, 1.5],   # North-East
             [ 0,  1, 1.0],   # East
             [ 1,  1, 1.5],   # South-East
             [ 1,  0, 1.0],   # West
             [ 1, -1, 1.5],   # South-West
             [ 0, -1, 1.0]]   # West

    warehouse[dropzone[0]][dropzone[1]] = 0
    print("MAP")
    for i in range(len(warehouse)):
        print(warehouse[i])
    print("")

    # Go through the map, and store locations of all the boxes
    for x in range(len(warehouse)):
        for y in range(len(warehouse[0])):
            if (warehouse[x][y] > 0):
                box_locations[warehouse[x][y]] = [x,y]

    for i in range(len(todo)):
        
        print("Looking for box # " + repr(todo[i]) )
        box_location = box_locations[todo[i]]
        print("    Box # " + repr(todo[i]) + " is located at " + repr(box_location))

        # Calculate the heuristic
        heuristic = [[99 for col in range(len(warehouse[0]))] for row in range(len(warehouse))]
        change = True
        while(change):
            change = False
            for x in range(len(warehouse)):
                for y in range(len(warehouse[0])):
                   
                    if((box_location[0] == x) and (box_location[1] == y)):
                        heuristic[x][y] = 0
                    elif(warehouse[x][y] == 0):
                        for a in range(len(delta)):
                            x2 = x + delta[a][0]
                            y2 = y + delta[a][1]

                            if((x2 >= 0) and (x2 < len(warehouse)) and (y2 >= 0) and (y2 < len(warehouse[0]))):
                                if(heuristic[x][y] > (heuristic[x2][y2] + delta[a][2])):
                                    heuristic[x][y] = heuristic[x2][y2] + delta[a][2]
                                    change = True

                
        print("Heuristic is")
        for i in range(len(warehouse)):
            print(heuristic[i])

        # Run A*
        print("\n\nRunning A*")
        expand = [[-1 for col in range(len(warehouse[0]))] for row in range(len(warehouse))]
        closed = [[0 for col in range(len(warehouse[0]))] for row in range(len(warehouse))]
        closed[dropzone[0]][dropzone[1]] = 1
        

        # create a list of "search sets"
        # each row contains a search path
        # each element contains x,y,cost_from_last_cell
        search_set = [[]]

        x = dropzone[0]
        y = dropzone[1]
        g = 0
        f = g + heuristic[x][y]
        s = 0                     # current search set

        open = [[f, g, x, y, s]]
        search_set[0].append([x,y,0])
        #search_set[0] = 0

        found = False
        resign = False

        while not found and not resign:
            first_empty_cell_found = False

            if len(open) == 0:
                resign = True

            else:
                open.sort()
                open.reverse()
                next = open.pop()
                x = next[2]
                y = next[3]
                g = next[1]
                f = g + heuristic[x][y]
                s = next[4]
                print("Next item on open stack is " + repr(next))


                if((x == box_location[0]) and (y == box_location[1])):
                    found = True
                    warehouse[x][y] = 0
                    print("")
                    print("Found box. Calculating Cost")
                    # Count cost
                    #current_cost = search_set[s] 
                    current_cost = count_path_cost(search_set[s])
                    print("Current cost to box and back is " + repr(current_cost))
                    cost += (2 * current_cost)
                else:
                    print("else")
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        print("Else: [x2,y2] = [" + repr(x2) + "," + repr(y2) + "]")
                        if((x2 >= 0) and (x2 < len(warehouse)) and (y2 >= 0) and (y2 < len(warehouse[0]))):
                            if(((closed[x2][y2] == 0) and (warehouse[x2][y2] == 0)) or
                               ((x2 == box_location[0]) and (y2 == box_location[1]))):
                                if(first_empty_cell_found == True):
                                    s = add_new_search_path(search_set,s)
                                    print("Forked search_path")
                                    for z in range(len(search_set)):
                                        print("\t" + repr(search_set[z]))
                                first_empty_cell_found = True
                                g2 = g + delta[i][2]
                                f2 = g2 + heuristic[x2][y2]
                                open.append([f2, g2, x2, y2, s])
                                print("    adding [" + repr(x2) + "," + repr(y2) + "] to the stack")
                                closed[x2][y2] = 1
                                search_set[s].append([x2,y2,delta[i][2]])
                                #search_set[s] = search_set[s] + (2 * delta[i][2])
                                print("Adding " + repr(delta[i][2]) + " cost to search_set " + repr(s) + ". Search_set " + repr(s) + " is " + repr(search_set[s]))

        print("")
        print("Current cost: " + repr(cost))
        print("*************************")

    return cost
   
def add_new_search_path(search_set, s):
    # appends a row to search_set, and copies row s to it (ignoring last element in row)
    # returns: row number s
    #search_set.append(search_set[s])
    search_set.append(search_set[s][:-1])
   
    return (len(search_set) - 1)

def count_path_cost(goal_path):
    temp_cost = 0

    for i in range(len(goal_path)):
        temp_cost += goal_path[i][2]
        
    return temp_cost
 
################# TESTING ##################
       
# ------------------------------------------
# solution check - Checks your plan function using
# data from list called test[]. Uncomment the call
# to solution_check to test your code.
#
def solution_check(test, epsilon = 0.00001):
    answer_list = []
    
    import time
    start = time.clock()
    correct_answers = 0
    for i in range(len(test[0])):
        user_cost = plan(test[0][i], test[1][i], test[2][i])
        true_cost = test[3][i]
        if abs(user_cost - true_cost) < epsilon:
            print "\nTest case", i+1, "passed!"
            answer_list.append(1)
            correct_answers += 1
            #print "#############################################"
        else:
            print "\nTest case ", i+1, "unsuccessful. Your answer ", user_cost, "was not within ", epsilon, "of ", true_cost 
            answer_list.append(0)
    runtime =  time.clock() - start
    if runtime > 1:
        print "Your code is too slow, try to optimize it! Running time was: ", runtime
        return False
    if correct_answers == len(answer_list):
        print "\nYou passed all test cases!"
        return True
    else:
        print "\nYou passed", correct_answers, "of", len(answer_list), "test cases. Try to get them all!"
        return False
#Testing environment
# Test Case 1 
warehouse1 = [[ 1, 2, 3],
             [ 0, 0, 0],
             [ 0, 0, 0]]
dropzone1 = [2,0] 
todo1 = [2, 1]
true_cost1 = 9
# Test Case 2
warehouse2 = [[   1, 2, 3, 4],
             [   0, 0, 0, 0],
             [   5, 6, 7, 0],
             [ 'x', 0, 0, 8]] 
dropzone2 = [3,0] 
todo2 = [2, 5, 1]
true_cost2 = 21

# Test Case 3
warehouse3 = [[  1, 2, 3, 4, 5, 6, 7],
             [   0, 0, 0, 0, 0, 0, 0],
             [   8, 9,10,11, 0, 0, 0],
             [ 'x', 0, 0, 0,  0, 0, 12]] 
dropzone3 = [3,0] 
todo3 = [5, 10]
true_cost3 = 18

# Test Case 4
warehouse4 = [[  1,17, 5,18, 9,19, 13],
             [   2, 0, 6, 0,10, 0, 14],
             [   3, 0, 7, 0,11, 0, 15],
             [   4, 0, 8, 0,12, 0, 16],
             [   0, 0, 0, 0, 0, 0, 'x']] 
dropzone4 = [4,6] 
todo4 = [13, 11, 6, 17]
true_cost4 = 41

testing_suite = [[warehouse1, warehouse2, warehouse3, warehouse4],
                 [dropzone1, dropzone2, dropzone3, dropzone4],
                 [todo1, todo2, todo3, todo4],
                 [true_cost1, true_cost2, true_cost3, true_cost4]]


solution_check(testing_suite) #UNCOMMENT THIS LINE TO TEST YOUR CODE


