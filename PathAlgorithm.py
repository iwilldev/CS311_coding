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

def _getSmallestNot(array, notin):
    currentLeast = float('inf')
    for iterable in array:
        if iterable > 0 and iterable < currentLeast and iterable not in notin:
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
    #nodes = [curNode]

    #we set the first point in the table to 0, since we pick it first.
    distanceTable[curNode] = 0

    # loop through each node in the adjacency matrix.
    # Only the number of times matters as the order may differ
    for i in range(length):

        #first we add our current node to the visited list
        nodes.append(curNode)

        #Loop through each visited node
        for eachNode in nodes:
            #we now loop through all node connections for curNode in the adjacency matrix
            for connection in range(length):

                # Set item to the currently inspected weight
                item = int(graph[eachNode][connection])

                #insert item at its index to the distance table if it is not zeroed out
                #our distance table updates as we gain more nodes
                if item > 0 and connection not in nodes:
                    if item < distanceTable[connection] or distanceTable[connection] == -1:
                        distanceTable[connection] = item

        # Get the smallest available edge weight / distance
        currentLeast = _getSmallest(distanceTable)
        
        # we get the index of the smallest distance found for the current node
        # and store it as nextNode
        
        nextNode = distanceTable.index(currentLeast)

        #add to the mst
        mst.add((curNode,nextNode)) 


        #print info
        print("****Iteration****")
        print("Table:", distanceTable)

        print("Pulling: ",currentLeast)
        print("Node: (n) ", curNode)
        
        print("NodeList: ", nodes)
        print("MST: ", mst)
        # Since we just pulled the smallest distance, we can remove it from the distance table
        distanceTable[nextNode] = 0

        #print(smallestBranch)
        print("curNode: ", curNode)
        print("nextNode: ", nextNode)
        
        # progress forward by iterating the curNode variable to the next node
        curNode = nextNode
    print(nodes)
    return mst

        

def totalWeight(mst, graph):
    pass

def edgeNames(mst,graph):
    pass