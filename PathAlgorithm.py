# PathAlgorithm.py
# Written by Alex Barbee

from WeightedGraph import WeightedGraph
import numpy as np

def _getSmallest(array):
    currentLeast = float('inf')
    for iterable in array:
        if iterable > 0 and iterable < currentLeast:
            currentLeast = iterable
    if currentLeast == float('inf'):
        return 0
    return currentLeast

def _getSmallestNot(array, notint):
    currentLeast = float('inf')
    for iterable in array:
        if iterable > 0 and iterable < currentLeast and iterable != notint:
            currentLeast = iterable
    if currentLeast == float('inf'):
        return 0
    return currentLeast

def prim(WeightedGraphObj):
    mst = set()
    
    nodes = []
    graph = WeightedGraphObj.matrix
    # Get the shape of the adjacency matrix
    length = graph.shape[0]

    distanceTable = [-1] * length

    # initialize the currentnode to the first node in the set
    curNode = 0
    # for now we do not know the next node so we initialize it as the currentnode
    nextNode = curNode  

    # here, we add the current node as the first item in the node list
    # because we have to start from somewhere
    nodes = [curNode]

    #we set the first point in the table to 0, since we pick it first.
    distanceTable[curNode] = 0

    #loop through each node, and perform the algorithm
    for i in range(length):
        for k in range(length):
            # here we get the weight from the current edge (of many) branching from the current node
            item = int(graph[curNode][k])

        
            if item > 0:
                if item < distanceTable[k] or distanceTable[k] == -1:
                    distanceTable[k] = item

        currentLeast = _getSmallest(distanceTable)
        
        # we get the index of the smallest distance found for the current node
        # and store it as nextNode
        print(currentLeast)
        nextNode = distanceTable.index(currentLeast)

        print("after:")
        print(distanceTable)

        # Since we just pulled the smallest distance, we can remove it from the distance table
        distanceTable[nextNode] = 0


        #append the nextNode to the node list
        if len(nodes) <= length-1:
            nodes.append(nextNode)

        #here, we get the node with the smallest branch
        smallestBranch = float('inf')
        for each in nodes:
            possible = _getSmallestNot(graph[each],each)
            if possible < smallestBranch:
                smallestBranch = possible
        mst.add((curNode,nextNode))



        # progress forward by iterating the curNode variable to the next node
        curNode = nextNode
    print(nodes)
    return mst

        

def totalWeight(mst, graph):
    pass

def edgeNames(mst,graph):
    pass