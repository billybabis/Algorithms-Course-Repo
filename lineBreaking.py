## Algorithms HW5 #1 Line Breaking
## Billy Babis
## November 2015

#This is a classic dynamic programming example. The problem is that we have a
# text editor that allows X number of characters on each line. We must figure
# out how to arrange the words in order to minimize the total number of lines
# in the document

#For example, if we have the words ["I", "love", "programming", "in", "overalls"]
# with X=12 letters per line:
# we would want the orientation to be
# line1:  "I love"
# line2:  "programming"
# line3:  "in overalls"

##This dynamic programming solution generates a iterates through each breakpoint,
## keeping track of the cheapest path to arrive there. 

def linebreaking(sentence, length): 
    words = sentence.split(' ')                 #create a list of all the words
    currBPmins = rightMostBP(words, length)     #list of costs if right-most break-point is placed at i
    psiArray = generatePsiArray(words, length)  #2d-array showing cost of 2 adjacent breakpoints
    breakpoints = []                            #keep track of our optimal breakpoints
# This dynamic programming solution generates a

def linebreaking(sentence, length): 
    words = sentence.split(' ')
    currBPmins = rightMostBP(words, length)
    psiArray = generatePsiArray(words, length)
    breakpoints = []
    ##Loop through our psi array and keep track of all of the break point indeces
    for i in range(len(words)-2):
        currBPmins, indeces = minCostAtIndeces_nextBP(currBPmins, psiArray)
        breakpoints.append(indeces)

    leftBP = leftMostBP(words, length)
    minBP, index = finalBP_determination(leftBP, currBPmins)
    minBPpath = findBPpath(index, breakpoints)

    printBreaks(words, minBPpath)

##This is essentially the first psi function being fired for the N-1 break point
## We need to figure out where to put our last (right-most) breakpoint. In order to
## do this, we will generate a list containing the cost at each given breakpoint.
## For example, if we have a sentence with 4 words, we have 4 possible breakpoints in
## in between each word. If the output=[None, None, 1, 6], that means the cost of
## of putting our last breakpoint at location 2 is output[2]=1. 
def rightMostBP(words, length):
    costs = []
    for i in range(1, len(words)+1):
        lengths = [len(words[j])+1 for j in range(i,len(words))]
        cost1 = sum(lengths)
        if cost1 > length: costs.append(None)
        elif cost1==0: costs.append(0)
        else: costs.append(length-cost1)
    return costs

##last psi opertaion for the left most break point
def leftMostBP(words, length):
    costs=[]
    for i in range(1,len(words)+1):
        lengths = [len(words[j])+1 for j in range(0,i)]
        sum1=sum(lengths)
        if sum1>length: costs.append(None)
        else: costs.append(sum1)
    return costs

#generates a 2d array of costs for partiuclar sequences of breakpoints
# i.e. output[0][3] will show us the cost associated with 2 consecutive
# breakpoints placed at locaiton 0 and location 3
#generates a 2d array of costs for partiuclar sequences of breakpoints 
def generatePsiArray(words, length):
    costsOfBreakPoints = [[None]*len(words) for i in range(len(words))]
    for i in range(1,len(words)+1):
        for j in range(1, len(words)+1):
            costsOfBreakPoints[i-1][j-1] = cost(words, length, i, j)
    return costsOfBreakPoints

#finds the cost for the 2 given consecutive breakpoints
def cost(words, length, r, c):
    if (r == c): return 0
    elif (r > c): return None
    else:
        lengths = [len(words[i]) for i in range(r, c)]
        if sum(lengths) > length: return None
        else: return length - sum(lengths)

#different cost functions           
def cost_i(i,j):return i+j
def cost_ii(i,j): return i**2 + j**2
def cost_iii(i,j): return i**.5+j**.5

def minCostAtIndeces_nextBP(costs, phiArray):
    costs_pathToI = []
    listOfMins, indeces = [],[]
    for i in range(len(costs)):
        for j in range(len(costs)):
            if (phiArray[i][j]==None or costs[j]==None):
                costs_pathToI.append(None)
            else:
                costs_pathToI.append(cost_i(costs[j],phiArray[i][j]))
                
        minVal,index = findMin(costs_pathToI)
        listOfMins.append(minVal)
        indeces.append(index)
        costs_pathToI = []
    return listOfMins, indeces

def findMin(costs):
    min1, index = None, None
    for i in range(len(costs)):
        if costs[i]!=None:
            if min1 > costs[i] or min1==None:
                min1 = costs[i]
                index = i+1
            elif costs[i] == min1:
                temp = []
                temp.append(index)
                temp.append(i+1)
                index = []
                for ind in temp:
                    index.append(ind)
    return min1, index


def finalBP_determination(costsOfLeftMostBP, allOtherBPcosts):
    min1, index = None, []
    for i in range(len(costsOfLeftMostBP)):
        leftBPcost = costsOfLeftMostBP[i]
        nextBPcost = allOtherBPcosts[i]
        if leftBPcost!=None and nextBPcost!=None:
            if min1==None or min1>(leftBPcost+nextBPcost):
                min1 = leftBPcost + nextBPcost
                index.append(i+1)
            elif min1==(leftBPcost + nextBPcost):
                index.append(i+1)
    return min1, index

def findBPpath(leftBP, breakPoints):
    if isinstance(leftBP,list):
        leftBP = leftBP[0]
    BPs=[]
    for i in range(len(breakPoints)):
        while isinstance(leftBP, list):
            leftBP=leftBP[0]
        BPs.append(leftBP-1)
        leftBP = breakPoints[len(breakPoints)-i-1][leftBP-1]
    if isinstance(leftMostBP, list):
        leftBP = leftBP[0]
    BPs.append(leftBP-1)
    return BPs

def printBreaks(words, bpPath):
    bpPath = clearRepeats(bpPath)
    ctr = 0 
    for i in range(len(bpPath)):
        bp = bpPath[i]+1
        line = ""
        while ctr < bp:
            line = line + " " + words[ctr]
            ctr += 1
        print line
    if ctr < len(words):
        line = ""
        for word in words[ctr:]:
            line = line + " " + word
        print line

def clearRepeats(bps):
    lst = [bps[0]]
    for bp in bps[1:]:
        if bp not in lst:
            lst.append(bp)
    lst.remove(0)
    return lst
        
str1 = "Some kinds of writing work best in long paragraphs, and others move through many short paragraphs. Newspaper reporters usually write in very short paragraphs. In addition, their examples and explanations are not always tightly tied in related clusters. This style of writing is addressed to readers who are skimming and looking for the main points in the first few inches of print, so reporters dont develop each idea fully in clear sequence. Information in newspaper articles sometimes has to be reorganized to make a standard essay"
linebreaking(str1, 30)

#import urllib2
#data = urllib2.urlopen('http://www.mieliestronk.com/corncob_caps.txt')
#str2=""
#for word in data.read().split()[:500]:
#    str2 = str2 + " " + word
#linebreaking(str2,70)

## N = [10,100, 500]
## t = [.147,1.187,67.41]
## t/N^2 = [.00147, .0001187,.000270]
