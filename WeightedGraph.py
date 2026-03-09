# WeightedGraph.py
# Written by Alex Barbee

import numpy as np

class WeightedGraph:
    def __init__(self, fname):
        __fileName__ = fname

        __fObj__ = open(self.fileName)

        #read the line, strip newline character, split into a list
        # and pass into arrray initializer
        self.names = np.array(__fObj__.readline().strip().split(',') )

        # just stores the size as an integer
        # so we don't call functions needlessly
        self.side = self.names.size

        #initialize matrix as a matrix of -1
        self.matrix = np.full((self.side, self.side),-1)

        #Matrix setup code

        for line in __fObj__:
            
            # split line into array
            dat = line.strip().split(',')



        # Close file after working with it
        __fObj__.close()

    # Calculates the weight of the edge between nodes
    # @i and @k, and results in -1 if they do not exist
    # @return: a float value being the weight
    def getWeight(i, k):
        pass

    # Checks whether an edge exists between @i and @k
    # or if @i and @k are the same node
    # @return: A boolean value if edge exists
    def directLink(i,k):
        pass
    
    # Gets the name of a node associated with 
    # the given index @i
    # @return: A string being the name of the node
    def getNodeName(i):
        pass

    # Gets the current number of nodes in the graph
    # @return an integer count of nodes
    def getSize():
        pass