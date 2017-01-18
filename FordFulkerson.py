## HW6 Ford-Fulkerson's Algorithm --> max flow
## Billy Babis
## December 2015

##The Ford-Fulkerson Algorithm finds the maximal flow in a directed graph
## where each edge has a maximal flow value. Given each edge in between
## the startNode (souce) and endNode (sink), we need to find the maximal flow.
## This algorithm can use either Breath-First Search or Depth-First Search to
##  find the path from source to sink.

## The method for accomplishing this is a greedy solution to try all paths from
## source to sink. After we compute the flow accross a path, we create a new
## residual graph excluding the path just computed. The method is applied again
## to the residual graph until exhausted. 

graph1 = [{1:25,2:30},{3:40},{3:20,4:35},{5:60},{5:45},{}]
#==> graph[0][1] = 25 = flow capacity of path from 0 to 1
#source=0,sinkt=5


def dfs_toSink(graph, source, sink):
    visited = []
    stack=[source]
    while sink not in visited:
        if stack==[]:
            return None
        v = stack.pop()
        if v not in visited:
            visited.append(v)
        for v2 in graph[v]:
            if v2 not in visited:
                stack.append(v2)
    return visited

def bfs_toSink(graph, source, sink):
    visited = []
    queue=[source]
    while sink not in visited:
        if queue==[]:
            return None
        v = queue[0]
        del queue[0]
        if v not in visited:
            visited.append(v)
        for v2 in graph[v]:
            if v2 not in visited:
                queue.append(v2)
    return visited

def createGf(graph, pathToSink, maxFlow):
    for i in range(len(pathToSink)-1):
        v1 = pathToSink[i]
        v2 = pathToSink[i+1]
        graph[v1][v2] = graph[v1][v2] - maxFlow
        if graph[v1][v2]==0:
            del graph[v1][v2]
        if v1 in graph[v2]:
            graph[v2][v1] = graph[v2][v1] + maxFlow
        else:
            graph[v2][v2] = maxFlow
    return graph
    
def fordFulkerson(graph, source, sink):
    flow = 0
    while(True):
        print "Current Graph: " + str(graph)
        pathToSink = dfs_toSink(graph, source, sink)
        ##means we have exhausted our residual graph
        if pathToSink==None:
            break
        maxFlow = None 
        for i in range(len(pathToSink)-1):
            v1 = pathToSink[i]
            v2 = pathToSink[i+1]
            capacity = graph[v1][v2]
            if capacity < maxFlow or maxFlow == None:
                maxFlow = capacity
        if maxFlow == 0:
            break
        createGf(graph, pathToSink, maxFlow)
        flow+=maxFlow
    return flow           
        

print fordFulkerson(graph1, 0, 5)
