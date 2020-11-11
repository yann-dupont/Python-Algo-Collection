
# Common graph algos implementations.

from collections import deque
from queue import PriorityQueue

from graphUtils import *

# Scrolls the graph breadth first, with a queue :
# each iteration, takes the first node of the queue,
# and adds its unchecked neighs to the queue.
# Condition : Every edge has the same cost, else see Topo_DAG.
# adjList :     list[list[tuple(int, int)]] adjacence list of the graph
# start :       int starting node index
# returns : list[int], predecessor list : for every node, the node before it when coming from start node
# alternatively : list[int], distance list : for every node, the distances between the start node and it
# O(n + p)
def BFS(adjList, start) :
    nNodes = len(adjList)
    nodesColor = [0 for i in range(nNodes)] # 0 if currently unchecked, 1 if done
    pred = [-1 for i in range(nNodes)]
    distances = [-1 for i in range(nNodes)]
    distances[start] = 0
    grayQ = deque([start])

    while grayQ :
        curNode = grayQ.popleft()
        for neigh in adjList[curNode] :
            if not nodesColor[neigh[0]] and neigh[0] not in grayQ :
                grayQ.append(neigh[0])
                pred[neigh[0]] = curNode
        nodesColor[curNode] = 1
        if curNode != start :
            distances[curNode] = distances[pred[curNode]] + 1

        # you may add current node processing here
        #print(curNode)

    return pred
    # return distances

# Scrolls the graph breadth first, with a heap :
# each iteration, takes the first node of the heap,
# and adds its unchecked neighs to the heap.
# Condition : None
# adjList :     list[list[tuple(int, int)]] adjacence list of the graph
# start :       int starting node index
# returns : list[int], predecessor list : for every node, the node before it when coming from start node
# alternatively : list[int], topological numerotation list :
#                 for every rank, the corresponding node according to topological sorting
# O(n + p)
def DFS(adjList, start) :
    nNodes = len(adjList)
    nodesColor = [0 for i in range(nNodes)] # 0 if currently unchecked, 1 if done
    pred = [-1 for i in range(nNodes)]
    topoNum = [-1 for i in range(nNodes)]
    curTopoNum = 0
    grayQ = deque([start])

    while grayQ :
        curNode = grayQ.pop()
        for neigh in adjList[curNode][::-1] :
            if not nodesColor[neigh[0]] and neigh[0] not in grayQ :
                grayQ.append(neigh[0])
                pred[neigh[0]] = curNode
        nodesColor[curNode] = 1
        topoNum[curTopoNum] = curNode
        curTopoNum += 1

        # you may add current node processing here
        #print(curNode)

    return pred
    # return topoNum

# Scrolls the graph in the topological sorting order.
# Condition : The graph is a DAG (Directed Acyclic Graph), else see Dijkstra.
# adjList :     list[list[tuple(int, int)]] adjacence list of the graph
# start :       int starting node index
# returns : list[int], predecessor list : for every node, the node before it when coming from start node
# alternatively : list[int], distance list : for every node, the distances between the start node and it
# O(n + p)
def Topo_DAG(adjList, start) :
    topoNum = DFS(adjList, start) # get topological sorting
    nNodes = len(adjList)
    pred = [-1 for i in range(nNodes)]
    distances = [-1 for i in range(nNodes)]
    distances[start] = 0

    for n in range(nNodes) :
        for neigh in adjList[topoNum[n]] :
            if distances[topoNum[n]] + neigh[1] < distances[neigh[0]] or distances[neigh[0]] == -1 :
                distances[neigh[0]] = distances[topoNum[n]] + neigh[1]
                pred[neigh[0]] = topoNum[n]

        # you may add current node processing here
        #print(curNode)

    return pred
    # return distances


# Scrolls the graph breadth first, with a priority queue, according to the distance between start and current node :
# each iteration, takes the first node of the queue,
# and adds its unchecked neighs to the queue.
# Condition : No negative cost edge, else see Bellman-Ford.
# adjList :     list[list[tuple(int, int)]] adjacence list of the graph
# start :       int starting node index
# returns : list[int], predecessor list : for every node, the node before it when coming from start node
# alternatively : list[int], distance list : for every node, the distances between the start node and it
# O((n+p)log(n))
def Dijkstra(adjList, start) :
    nNodes = len(adjList)
    nodesList = [None for i in range(nNodes)]  # O(n)
    nodesColor = [0 for i in range(nNodes)]  # O(n)
    for i in range(nNodes) :  # O(n)
        nodesList[i] = Node(i, adjList[i])
    pred = [-1 for i in range(nNodes)]  # O(n)
    distances = [-1 for i in range(nNodes)]  # O(n)
    distances[start] = 0

    grayQ = PriorityQueue()
    nodesList[start].distance = 0
    grayQ.put(nodesList[start])  # O(log(n))

    while not grayQ.empty() :  # O(n)
        curNode = grayQ.get()  # O(log(n))

        for neighTuple in curNode.voisins :  # O(p/n)
            neigh = nodesList[neighTuple[0]]
            if neigh.distance == -1 or neigh.distance > curNode.distance + neighTuple[1] :
                neigh.distance = curNode.distance + neighTuple[1]
                distances[neigh.num] = curNode.distance + neighTuple[1]
                pred[neigh.num] = curNode.num
                if nodesColor[neigh.num] == 0 :
                    grayQ.put(neigh)  # O(log(n))
                    nodesColor[neigh.num] = 1

        # you may add current node processing here
        #print(curNode)

    return pred
    # return distances

# A* ?
# Variable complexity

# Bellman_Ford
# O(n * p)

# Floyd-Warshall
# O(n^3)

# Calculates the Min Span Tree.
# Condition : None ?
# adjList :     list[list[tuple(int, int)]] adjacence list of the graph
# start :       int starting node index
# returns : list[tuple(int, int, int)], list of all edges (indexNodeA, indexNodeB, edgeCost) of the Min Span Tree
# O(n * log(p))
def Kruskal(nNodes, edgeList):
    treeList = [[i] for i in range(nNodes)]
    treeEdges = [[] for i in range(nNodes)]
    edgesWeight = [edgeList[i][2] for i in range(len(edgeList))]

    nbTours = 0
    while(True) :
        nbTours += 1
        if min(edgesWeight) == 1000000 or len(treeList) == 1 :
            break

        minWeightIndex = edgesWeight.index(min(edgesWeight))
        edgesWeight[minWeightIndex] = 1000000
        nodeD = edgeList[minWeightIndex][0]
        nodeA = edgeList[minWeightIndex][1]
        treeD = 0
        treeA = 0

        for i in range(len(treeList)) :
            for j in range(len(treeList[i])) :
                if treeList[i][j] == nodeD :
                    treeD = i
                if treeList[i][j] == nodeA :
                    treeA = i
                if treeD != 0 and treeA != 0 :
                    break

        if treeA == treeD :
            # we found 2 identical trees
            continue

        treeToAdd = treeList[treeA]
        treeToRemove = treeList[treeD]
        edgesToAdd = treeEdges[treeA]
        edgesToRemove = treeEdges[treeD]

        # we fusion the 2 trees : treeToRemove and treeToAdd
        for node in treeToRemove :
            treeToAdd.append(node)
        edgesToAdd.append((nodeA, nodeD, edgeList[minWeightIndex][2]))
        for ar in edgesToRemove :
            edgesToAdd.append(ar)

        treeList.remove(treeToRemove)
        treeEdges.remove(edgesToRemove)

    s = 0
    for edge in treeEdges[0] :
        s += edge[2]

    return treeEdges # edges of the Min Span Tree
    # return s # sum of the values of the edges of the Min Span Tree




# --- testing code ---

# nNodes = 6
# edgesList = [[0, 1], [1, 2], [2, 3], [0, 4]]
# start = 0
# adjList = edgeListToAdjList(edgesList, nNodes)
# print(BFS(adjList, start))
# --- results :
# --- pred = [-1, 0, 1, 2, 0, -1]
# --- distances = [0, 1, 2, 3, 1, -1]


# nNodes = 18
# edgesList = [[0, 1], [1, 2], [0, 3], [0, 4], [4, 3], [2, 5], [5, 6], [2, 7], [4, 8], [4, 9], [9, 10], [0, 11], [11, 12], [0, 13], [6, 14], [0, 15], [2, 16], [16, 17]]
# start = 0
# adjList = edgeListToAdjList(edgesList, nNodes)
# print(DFS(adjList, start))
# --- results :
# --- pred = [-1, 0, 1, 0, 0, 2, 5, 2, 4, 4, 9, 0, 11, 0, 6, 0, 2, 16]
# --- topoNum = [0, 1, 2, 5, 6, 14, 7, 16, 17, 3, 4, 8, 9, 10, 11, 12, 13, 15]

# nNodes = 18
# edgesList = [[0, 1, 3], [1, 2, 5], [0, 3, 2], [0, 4, 4], [4, 3, 7], [2, 5, 10], [5, 6, 11], [2, 7, 1], [4, 8, 7], [4, 9, 4], [9, 10, 5], [0, 11, 5], [11, 12, 5], [0, 13, 8], [6, 14, 16], [0, 15, 11], [2, 16, 2], [16, 17, 6]]
# start = 0
# adjList = edgeListToAdjList(edgesList, nNodes)
# print(DFS(adjList, start))
# --- results :
# --- pred = [-1, 0, 1, 0, 0, 2, 5, 2, 4, 4, 9, 0, 11, 0, 6, 0, 2, 16]
# --- topoNum = [0, 1, 2, 9, 10, 3, 4, 6, 11, 12, 13, 14, 15, 16, 5, 17, 7, 8]
# --- We expect the same as the previous test, since edge weight has no influence on DFS


# nNodes = 18
# edgesList = [[0, 1, 3], [1, 2, 5], [0, 3, 2], [0, 4, 4], [4, 3, 7], [2, 5, 10], [5, 6, 11], [2, 7, 1], [4, 8, 7], [4, 9, 4], [9, 10, 5], [0, 11, 5], [11, 12, 5], [0, 13, 8], [6, 14, 16], [0, 15, 11], [2, 16, 2], [16, 17, 6]]
# start = 0
# adjList = edgeListToAdjListWithCost(edgesList, nNodes)
# print(Topo_DAG(adjList, start))
# --- results :
# --- pred = [-1, 0, 1, 0, 0, 2, 5, 2, 4, 4, 9, 0, 11, 0, 6, 0, 2, 16]
# --- distances = [0, 3, 8, 2, 4, 18, 29, 9, 11, 8, 13, 5, 10, 8, 45, 11, 10, 16]


# nNodes = 10
# edgesList = [[0, 1, 85], [0, 2, 217], [7, 3, 183], [0, 4, 173], [1, 5, 80], [2, 6, 186], [2, 7, 103], [5, 8, 250], [4, 9, 502], [7, 9, 167], [8, 9, 84]]
# start = 0
# adjList = edgeListToAdjListWithCost(edgesList, nNodes)
# print(Dijkstra(adjList, start))
# --- results :
# --- pred = [-1, 0, 0, 7, 0, 1, 2, 2, 5, 7]
# --- distances = [0, 85, 217, 503, 173, 165, 403, 320, 415, 487]


# nNodes = 4
# edgelist = [[0, 1, 5], [0, 2, 3], [3, 0, 6], [1, 3, 7], [2, 1, 4], [2, 3, 5]]
# print(Kruskal(nNodes, edgelist))
# --- results :
# --- treeList = [[(3, 2, 5), (1, 2, 4), (2, 0, 3)]]
# --- s = 12

