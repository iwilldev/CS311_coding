# WeightedGraph.py
# Written by Alex Barbee

import numpy as np

class WeightedGraph:
    def __init__(self, fname):
        __fileName__ = fname

        __fObj__ = open(__fileName__)

        # read the line, strip newline character, split into a list
        # and pass into arrray initializer
        self.names = np.array(__fObj__.readline().strip().split(',') )

        # just stores the size as an integer
        # so we don't call functions needlessly
        self.side = self.names.size

        # initialize matrix as a matrix of -1
        self.matrix = np.full((self.side, self.side),-1)

        #Put zeroes for indices where the weight is going to be 0
        for ndx in range(self.side):
            self.matrix[ndx,ndx] = 0

        #Matrix setup code
        for line in __fObj__:
            
            # split line into array
            dat = line.strip().split(',')

            # get the node points and convert into numeric form
            xPos = np.where(self.names == dat[0])[0][0]
            yPos = np.where(self.names == dat[1])[0][0]
            
            # store the weight in a variable
            eWeight = dat[2]

            # set the values in the array for connected nodes
            self.matrix[xPos,yPos] = eWeight
            self.matrix[yPos,xPos] = eWeight

        # Close file after working with it
        __fObj__.close()

    # Calculates the weight of the edge between nodes
    # @i and @k, and results in -1 if they do not exist
    # @return: a float value being the weight
    def getWeight(self, i, k):
        return self.matrix[i,k]

    # Checks whether an edge exists between @i and @k
    # or if @i and @k are the same node
    # @return: A boolean value if edge exists
    def directLink(self,i,k):
        result = self.matrix[i,k]
        return (result > -1)
    
    # Gets the name of a node associated with 
    # the given index @i
    # @return: A string being the name of the node
    def getNodeName(self,i):
        return self.names[i]

    # Gets the current number of nodes in the graph
    # @return an integer count of nodes
    def getSize(self):
        return ((self.matrix > 0 ).sum())/2