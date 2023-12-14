import sys
from string import ascii_uppercase

# Aloocation Function with Parameter of the input file given in command line
def allocate(input = sys.argv[1], outputFile = sys.argv[2]):
    # Input file with graph
    graph = open(input,'r')
    # Stores nodes, their neighbours and their colours
    nodes = []
    neighbour = []
    # creates register and neighbour lists from the input file
    for i in graph:
        nodeList = i.split()
        nodes.append(nodeList[0])
        neighbour.append([])
        for j in i[1:].split():
            neighbour[-1].append(j)
    graph.close()

    # Rank the nodes, rank holds the number of neighbouring nodes, rankSort is rank sorted in desc, final ranks is the order of nodes to check
    rank = [len(x) for x in neighbour]
    rankSort = rank.copy()
    rankSort.sort(reverse=True)
    finalRanks = [None for i in rank]

    # Sort the nodes into their ranks based on number of neighbours
    for i in range(len(rankSort)):
        for j in range(len(rank)):
            # Check through the rank to find the equivalent node to the sorted ranks that isn't already in the final ranks
            if rankSort[i] == rank[j] and not(j in finalRanks):
                finalRanks[i] = j
                # break so that you use the lowest id in the case of 2 ranks being the same
                break

    # Stores colours and current node in final ranks
    colours = ['' for x in range(len(nodes))]
    currentNode = 0

    # Assign each node their colour starting with 
    for i in finalRanks:
        currentColour = 0
        # Stores the colours that the node cannot be
        neighbourColours = []
        # Check neighbour of nodes to assign colours
        for j in neighbour[i]:
            # Only check up to this current node in final rankings as any further won't have a colour
            if int(j)-1 in finalRanks[:currentNode]:
                neighbourColours.append(colours[int(j)-1])
        # loop through the colours until their is one that can be used
        while(ascii_uppercase[currentColour] in neighbourColours):
            currentColour = (currentColour + 1) % 26
        colours[i]=ascii_uppercase[currentColour]
        currentNode += 1

    # Write node allocation to file
    output = open(outputFile, 'w')
    for i in range(len(nodes)):
        output.write(nodes[i]+colours[i]+'\n')
    output.close()

    # Print output
    # output = open(outputFile,'r')
    # for i in output:
    #     print(i)
    # output.close()

        
allocate()