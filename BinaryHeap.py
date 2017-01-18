## Binary Heap
## Algorithms: HW3
## Billy Babis
## October, 2015

import math

# i)
## Using the efficient method we went over in class, we will build subtrees, starting
## from the bottom row, and then continue to work our way up a row until we reach the root element
## In the code below, we grab the index of the last (bottom-right most) parent, and then
## call the function sink to compare it with its child nodes recursively.
def heapify(lst):
    parentIndex = (len(lst)-2)/2
    while parentIndex >= 0:
        sink(lst, parentIndex)
        parentIndex=parentIndex-1
    return lst
            

## This function takes binary tree and the index of a parent node
## we continually compare this parent with its children and switch them if
## the value of the parent is greater than the value of the child
def sink(lst, index):
    lChild = (index+1)*2 - 1 
    rChild = lChild + 1
    ## this means our index is not a parent node
    if (lChild > len(lst)-1):
        return lst
    ## this means the leftChild is the last item in the array
    elif (rChild > len(lst)-1):
        if lst[lChild] < lst[index]:
            lst[lChild],lst[index] = lst[index],lst[lChild]
            return lst
    ## find the child with the smaller value and switch it with the parent node
    ## iff it is smaller in value than the parent node.
    ## call sink again on that parent node until it is a leaf node OR it is less
    ## than both children.
    else:
        smallerIndex = lChild if lst[lChild] < lst[rChild] else rChild
        if lst[smallerIndex] < lst[index]:
            lst[smallerIndex],lst[index] = lst[index],lst[smallerIndex]
            index = smallerIndex
            return sink(lst, index)
        else:
            return lst

#ii)

## To add, we place the number at the next array location and compare it with its parent node and switch
## them if the child < parent. Do this recursively (in the swim() function) until the child is the root OR
## the child > parent
def add(num, bHeap):
    bHeap.append(num)
    index = len(bHeap) - 1
    swim(index, bHeap)
    return bHeap

def swim(index, bHeap):
    if index == 0:
        return bHeap
    parent = (index-1)/2
    if bHeap[index] < bHeap[parent]:
        bHeap[index], bHeap[parent] = bHeap[parent], bHeap[index]
        return swim(parent, bHeap)
    else:
        return bHeap

# iii)
## Our remove method is to pop() the root element and replace it with the last item in the binary heap
## then, we must continually compare that new root element with its children until it is a leaf node
## OR it is less than both children
def remove(bHeap):
    pop = bHeap[0]
    bHeap[0] = bHeap[-1]
    del bHeap[-1]
    sink(bHeap, 0)
    return bHeap

# iv)
##In every binary heap, the root is the smallest value. Simply apply the function above if you want to pop it as well
def minVal(bHeap):
    return bHeap[0]

def prettyPrint(bh):
    size = len(bh)
    indents = size/2
    row = 1
    nextBreak = 2**row
    line = (indents+1)*"  " + str(bh[0])
    print line
    line = "  "*indents
    for i in range(1,size,1):
        line += " " + str(bh[i]) + ","
        if i==nextBreak:
            row+=1
            nextBreak = nextBreak + 2**row
            
            print line
            indents -= 1
            line=" "*indents
    

exampleList = [1,12,43,10,19,2,9,50,41,22]
bh = heapify(exampleList)
print bh
prettyPrint(bh)

