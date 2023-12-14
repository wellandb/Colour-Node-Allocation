import time
import sys

# Allocation Test
def allocationTest(data = sys.argv[1], testfile = sys.argv[2]):
    # Start timer
    start = time.time()
    # Has error occured?
    error = False
    # Input data and file to test
    input = open(data,'r')
    output = open(testfile, 'r')
    testContent = output.readlines()

    # For all the nodes on the graph
    for i in input:
        nodeList = i.split()
        # Get the rest of nodes on the input line 
        for j in nodeList[1:]:
            # Only check for nodes greater than the current node so that there are no repeat error cases for each direction
            if int(j) > int(nodeList[0]):
                # If the colours of the neighbouring nodes are the same return an error
                if testContent[int(j)-1][len(j)] == testContent[int(nodeList[0])-1][len(nodeList[0])]:
                    print('ERROR NEIGHBOURING NODES ASSIGNED TO SAME COLOUR:\n', testContent[int(nodeList[0])-1], testContent[int(j)-1])
                    # Change the error value to true
                    error = True
    # Check if test's pass or not
    if not(error):
        print("Test's have passed.")

    end = time.time()
    print("Took "+str(end-start)+" seconds")

if len(sys.argv) != 3:
  print("Run as allocatTest.py <input for allocate> <output for allocate> ")
  sys.exit(0)

allocationTest()