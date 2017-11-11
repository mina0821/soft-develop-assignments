import numpy as np
## @package Statistics
#  Calculate blablabla by implementing circleT.

## @brief Calculates the average radius of a list of CircleT objects
# @param circleList A list containing CircleT objects
# @return The average radius of all the CircleT objects in the list
def average(circleList):
    R = np.arange(0)
    for x in circleList:
        R = np.append(R, [x.radius()])
    return np.average(R)

## @brief Calculates the standard deviation of all the radii in a list of CircleT objects
# @param circleList A list containing CircleT objects
# @return The standard deviation of all the radii
def stdDev(circleList):
    R = np.arange(0)
    for x in circleList:
        R = np.append(R, [x.radius()])
    return np.std(R)

## @brief Calculates the descending ranks of CircleT objects based on radius. Ranks of equal valued radii will have consecutive rank values.
# @param circleList A list containing CircleT objects
# @return The descending ranks of CircleT objects based on radius
def rank(circleList):
    R = []
    for x in circleList:
        R.append(x.radius())
            
    Rank = range(1,len(R)+1)
    for x in range(len(R)):
        for i in range(len(R)):
            if(R[x] > R[i] and Rank[x] > Rank[i]):
                temp = Rank[x]
                Rank[x] = Rank[i]
                Rank[i] = temp
            if(R[x] < R[i] and Rank[x] < Rank[i]):
                temp = Rank[x]
                Rank[x] = Rank[i]
                Rank[i] = temp
    return Rank
