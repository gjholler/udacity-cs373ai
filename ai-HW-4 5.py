#!/usr/bin/python
from time import time


# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

#grid = [[0, 1, 0],
#        [0, 0, 0]]
grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
       
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def stochastic_value():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    num_loops = 0
    
    while change:
        num_loops += 1
        change = False
    #for z in range(50000):
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if((goal[0] == x) and (goal[1] == y)):
                    value[x][y] = 0
                    policy[x][y] = '*'
                elif(grid[x][y] == 0):
                    for a in range((len(delta))):
                        left_index = (a + 1) % len(delta)
                        right_index = (a - 1) % len(delta)
                        x2l = x + delta[left_index][0]
                        y2l = y + delta[left_index][1]
                        x2f = x + delta[a][0]
                        y2f = y + delta[a][1]
                        x2r = x + delta[right_index][0]
                        y2r = y + delta[right_index][1]
                        v2 = cost_step

                        # Make sure that the forward step is valid
                        if(x2f >= 0 and x2f < len(grid) and y2f >= 0 and y2f < len(grid[0]) and grid[x2f][y2f] == 0):
                            #if x2f < 0 or x2f >= len(grid) or y2f < 0 or y2f >= len(grid[0]) or grid[x2f][y2f] == 1:
                            #    v2 += failure_prob * collision_cost
                            #else: 
                            #    v2 = (value[x2f][y2f] * success_prob)
                                #grid[x2f][y2f] == 0:
                            v2 += (value[x2f][y2f] * success_prob)
                            
                            # Add probability of going left
                            if x2l < 0 or x2l >= len(grid) or y2l < 0 or y2l >= len(grid[0]) or grid[x2l][y2l] == 1:
                            #if x2l < 0 or x2l >= len(grid) or y2l < 0 or y2l >= len(grid[0]):
                                v2 += failure_prob * collision_cost
                            else:
                                v2 += (value[x2l][y2l] * failure_prob)

                            # Add probability of going right
                            if x2r < 0 or x2r >= len(grid) or y2r < 0 or y2r >= len(grid[0]) or grid[x2r][y2r] == 1:
                            #if x2r < 0 or x2r >= len(grid) or y2r < 0 or y2r >= len(grid[0]):
                                v2 += failure_prob * collision_cost
                            else:
                                v2 += (value[x2r][y2r] * failure_prob)
                                   
                            #v2 += cost_step
                            if(v2 < value[x][y]):
                                #print("    " + repr(v2) + " < " + repr(value[x][y]))
                                #print("v2 < v1. Set true")
                                change = True
                                value[x][y] = v2
                                policy[x][y] = delta_name[a]

#        print("Finished loop. Change is " + repr(change))
#        for i in range(len(grid)):
#            print value[i]
#        for i in range(len(grid)):
#            print policy[i]
    print("Executed loop " + repr(num_loops) + " times")
    return value, policy



[v,p] = stochastic_value()

for i in range(len(grid)):
    print v[i]


for i in range(len(grid)):
    print p[i]
