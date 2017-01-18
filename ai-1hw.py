#!/usr/bin/python3.2

p=[[1.0/20,1.0/20,1.0/20,1.0/20,1.0/20],
   [1.0/20,1.0/20,1.0/20,1.0/20,1.0/20],
   [1.0/20,1.0/20,1.0/20,1.0/20,1.0/20],
   [1.0/20,1.0/20,1.0/20,1.0/20,1.0/20]]
colors=[['red','green','green','red','red'],
        ['red','red','green','red','red'],
        ['red','red','green','green','red'],
		['red','red','red','red','red']]

measurements = ['green','green','green','green','green']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 0.7
p_move = 0.8


def sense(p,Z):
    returnMatrix=[]
    pHit = sensor_right
    pMiss = 1 - sensor_right
    s = 0

    for row in range(len(p)):
        q=[]
        for col in range(len(p[row])):
            hit = (Z == colors[row][col])
            newVal = (p[row][col] * (hit * pHit + (1-hit) * pMiss))
            q.append(newVal)
            s = s + newVal
        returnMatrix.append(q)

    # Normalize
    for row in range(len(p)):
        for col in range(len(p[row])):
            returnMatrix[row][col] = returnMatrix[row][col] / s
    
    return returnMatrix

def move(p,U):
    returnMatrix = []
    pExact = p_move
    pMiss = 1 - p_move

    for row in range(len(p)):
        q=[]
        for col in range(len(p[row])):
            x = (row - U[0]) % len(p)
            y = (col - U[1]) % len(p[row])
            s = pExact * (p[x][y])
            s = s + (pMiss * p[row][col])

            q.append(s)
        returnMatrix.append(q)
    return returnMatrix

# Main
for i in range(len(measurements)):
    p = move(p,motions[i])
    p = sense(p,measurements[i])

print(p)

