# python3
# time the program: time python3 build_heap.py
import sys
import time

def build_heap(data):
    swaps = []
    
    def siftDown(currentNode, nodeAmount, data):
        minIndex = currentNode
        leftChild = 2*currentNode + 1
        if leftChild < nodeAmount and data[leftChild] < data[minIndex]: # Check if the left child is smaller than the current node
            minIndex = leftChild # Set the minIndex to the left child
            
        rightChild = 2*currentNode + 2 # Can be replaced with leftChild + 1
        if rightChild < nodeAmount and data[rightChild] < data[minIndex]: # Check if the right child is smaller than the current node
            minIndex = rightChild # Set the minIndex to the right child
            
        if currentNode != minIndex: # If the current node is not the smallest node (has been swapped to a child node), we add the swap to the swaps list
            swaps.append((currentNode, minIndex))
            data[currentNode], data[minIndex] = data[minIndex], data[currentNode] # Swap the current node with the smallest node
            siftDown(minIndex, nodeAmount, data)
            
    
    amountOfNodes = len(data)
    for i in range(len(data) // 2 -1, -1, -1):
        siftDown(i, amountOfNodes, data)
    

    return swaps


def main():
    
    # We copy the input code from the previous problems and modify it
    print("File type input")
    inputType = input()
    print("Input type: " + inputType[:1])
    # Below file type check is very similar to the first problem, with some minor changes to account for the different input type and requirements
    if(inputType[:1] == "F"):
        #print("Input the name of the file you want to use for testing")
        fileName = input()
        
        # If the file name contains a then we return
        if("a" in fileName):
            return
        elif("tests/" not in fileName): # Add the test/ directory to the file name if it is not already there (for Autograding tests)
            fileName = "tests/" + fileName
        
        try:
            with open(fileName) as readableFile:
                # n - number of total nodes, a.k.a the first line of the input
                # data - the second line of the input, a list of integers separated by spaces
                n = int(readableFile.readline()) # Converts the first line to an integer
                data = list(map(int, readableFile.readline().split())) # Converts the second line to a list of integers
        except FileNotFoundError:
            print("Invalid file name or path")
            return
    elif(inputType[:1] == "I"):
        n = int(input()) # Number of nodes
        data = list(map(int, input().split())) # List of integers separated by spaces
    else:
        print("Invalid input character")
        return

    # Check if the number of nodes corresponds to the given list of integers
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # output the amount of swaps
    print(len(swaps))
    
    # output the swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
