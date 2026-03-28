# PathAlgorithm.py
# Written by Alex Barbee

from WeightedGraph import WeightedGraph

def prim(WeightedGraphObj):
    mst = set()
    
    nodes = []
    graph = WeightedGraphObj.matrix
    # Get the shape of the adjacency matrix
    length = graph.shape[0]

    distanceTable = [-1] * length

    # initialize the currentnode to the first node in the set
    curNode = 0

    #we set the first point in the table to 0, since we pick it first.
    distanceTable[curNode] = 0

    # We loop while there are still nodes we can visit. 
    # When there are no more, the curNode stays at -1 until the end of the loop iteration
    while curNode != -1:

        #first we add our current node to the visited list
        nodes.append(curNode)

        #prime the variables for the new iteration of the loop
        nextNode = -1
        curNode = -1
        currentLeast = float('inf')

        # Loop through **each node** within the **nodes** list and find the smallest connecting edge 
        # that has not already been traversed
        for eachNode in nodes:
            #we now loop through all node connections for curNode in the adjacency matrix
            for connection in range(length):

                # Set item to the currently inspected weight
                item = int(WeightedGraphObj.getWeight(eachNode,connection))
                
                if item > 0 and connection not in nodes:
                    #If we make it here, we have found a new smallest edge in an untraversed node
                    if item < currentLeast:
                        currentLeast = item
                        nextNode = connection
                        curNode = eachNode

                    #insert item at its index to the distance table if it is not zeroed out
                    #our distance table updates as we gain more nodes
                    if distanceTable[connection] == -1 or item < distanceTable[connection]:
                        distanceTable[connection] = item
                    


        #if we get negative 1, there are no more nodes to visit
        if nextNode != -1:
            #add the new smallest edge to the mst
            mst.add((curNode,nextNode)) 

        '''
        #print info
        print("****Iteration****")
        print("Table:", distanceTable)
        print("Pulling: ",currentLeast)
        print("Node: (n) ", curNode)
        print("NodeList: ", nodes)
        print("MST: ", mst)
        print("curNode: ", curNode)
        print("nextNode: ", nextNode)
        '''
        # Since we just pulled the smallest distance, we can remove it from the distance table
        distanceTable[nextNode] = 0

        # progress forward by iterating the curNode variable to the next node
        curNode = nextNode
    #print(nodes)
    return mst

        

def totalWeight(mst, graph):
    total = 0
    for tuple in mst:
        total += graph.getWeight(tuple[0],tuple[1])
    return total



def edgeNames(mst,graph):
    edges = []
    for tuple in mst:
        edge = [str(graph.names[tuple[0]]),str(graph.names[tuple[1]])]
        edges.append(edge)
     
    return edges