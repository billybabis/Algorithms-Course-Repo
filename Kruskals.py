## HW6 Kruskal's Alg --> Min Spanning Tree
## Billy Babis
## December 2015

##Kruskal's Algorithm is popular for finding the minimum spanning tree
## of an inputted weighted graph. The minimum spanning tree is the sub-tree
## of the inputted graph that touches each node with the lowest cost or weight

##Kruskal's algorithm simply sorts all the costs in the weighted graph
## and then adds the lowest available edge to our solution if it does not
## complete a cycle. I use a Union-Find solution to ensure that there is never a cycle

## This code demonstrates my implementations of Kruskal, quickSort, and Union-Find

import random

graph1 = [{1:30,2:35},{0:30,3:15},{0:35,3:20},{1:15,2:20}]
#==> graph[0][1] = cost from 1-->2

#lst=[[30,(0,1)],[35,(0,2)],[15,(1,3)],[20,(2,3)]]

def quickSort(lst):
    if len(lst)==1 or len(lst)==0:
        return lst
    pivot = random.randint(0,len(lst)-1)
    left=[]
    right=[]
    repeats=[]
    for i in lst:
        if i[0] == lst[pivot][0]:
            repeats.append(i)
        elif i [0] <= lst[pivot][0]: left.append(i)
        else: right.append(i)
    return quickSort(left) + repeats + quickSort(right)          

class UnionFind:
    def __init__(self,N):
        self.keysToSubgroups = {}
        self.verticesToKeys = {}
        self.neighbors = {}
        self.totalCost = 0
        
    def find(self, edge):
        v1=edge[0]
        v2=edge[1]
        if v1 not in self.verticesToKeys:
            self.verticesToKeys[v1]=v1
            self.keysToSubgroups[v1]=[v1]
            self.neighbors[v1] = []
        if v2 not in self.verticesToKeys:
            self.verticesToKeys[v2]=v2
            self.keysToSubgroups[v2]=[v2]
            self.neighbors[v2]=[]
        return self.verticesToKeys[v1],self.verticesToKeys[v2]

    def union(self, key1,key2,edge,cost):
        self.totalCost += cost
        self.neighbors[edge[0]].append(edge[1])
        self.neighbors[edge[1]].append(edge[0])
        g1 = self.keysToSubgroups[key1]
        g2 = self.keysToSubgroups[key2]
        if len(g1) > len(g2):
            for v in g2:
                g1.append(v)
                self.verticesToKeys[v] = key1
            self.keysToSubgroups[key1] = g1
        else:
            for v in g1:
                g2.append(v)
                self.verticesToKeys[v] = key2
            self.keysToSubgroups[key2] = g2          

    def printStuff(self):
        print self.neighbors, self.totalCost

    def finalTree(self):
        return self.neighbors
    def finalCost(self):
        return self.totalCost



def kruskal(graph):
    ##restructure graph and sort
    costsAndEdges = []
    edges = []
    for v in range(len(graph)):
        for v2 in graph[v].keys():
            if (v,v2) not in edges and (v2,v) not in edges:
                edges.append((v,v2))
                node = [graph[v][v2],(v,v2)]
                costsAndEdges.append(node)
    costsAndEdges = quickSort(costsAndEdges)
    print "Sorted (Cost, Edge) tuple: " + str(costsAndEdges)

    ##unionFind to create minSpanningTree
    uf = UnionFind(len(graph))
    for costEdge in costsAndEdges:
        cost = costEdge[0]
        edge = costEdge[1]
        key1,key2 = uf.find(edge)
        if key1 != key2:
            uf.union(key1,key2,edge,cost)
    print "Below, note the final cost, followed by the tree of edges"
    return uf.finalCost(), uf.finalTree()

print "Inputted Graph:" + str(graph1)

print kruskal(graph1)
