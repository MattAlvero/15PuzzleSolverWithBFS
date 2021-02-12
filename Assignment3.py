# Assignment 3 for CS 411
# Author: Matthew Alvero
# NetID: malver2
# UIN: 663738906
# Created on 02/07/21

import sys
from queue import Queue

sys.setrecursionlimit(10**6)

"""
Puzzle class to define the entire puzzle
"""
class puzzleNode:
    
    # attributes of the Node
    cost = 1 # all moves cost 1
    theBoardState = None
    children = []
    theParent = None
    emptySpaceIdx = None
    moveToGetHere = None

    def __init__(self, board, parent, action):
        # get the board states
        self.theBoardState = board
        # set the parent, must be given
        self.theParent = parent
        # set the action that got here
        self.moveToGetHere = action
        # find the empty space index on the array
        for i in range(len(self.theBoardState)):
            if self.theBoardState[i] == 0:
                self.emptySpaceIdx = i
                break

    def getLeftMove(self):
        # check if we can even move left
        if self.emptySpaceIdx == 0 or self.emptySpaceIdx % 4 == 0:
            pass
        # otherwise, get the left child
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.theBoardState
            # perform the left move by swaping values in the array
            temp = newState[self.emptySpaceIdx-1]
            newState[self.emptySpaceIdx - 1] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            self.children.append(puzzleNode(newState, self, 'L'))
    
    def getRightMove(self):
        # check if we can even move right
        if self.emptySpaceIdx % 3 == 0:
            pass
        # otherwise, get the right child
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.theBoardState
            # perform the right move by swaping values in the array
            temp = newState[self.emptySpaceIdx+1]
            newState[self.emptySpaceIdx + 1] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            self.children.append(puzzleNode(newState, self, 'R'))

    def getUpMove(self):
        # check if we can even move up
        if self.emptySpaceIdx in range(0,5):
            pass
        # otherwise, get the up child
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.theBoardState
            # perform the up move by swaping values in the array
            temp = newState[self.emptySpaceIdx-4]
            newState[self.emptySpaceIdx - 4] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            self.children.append(puzzleNode(newState, self, 'U'))


    def getDownMove(self):
        # check if we can even move down
        if self.emptySpaceIdx in range(12,16):
            pass
        # otherwise, get the down child
        else:
            # copy the state to a new variable to be used as the childs state after the move
            newState = self.theBoardState
            # perform the down move by swaping values in the array
            temp = newState[self.emptySpaceIdx+4]
            newState[self.emptySpaceIdx + 4] = newState[self.emptySpaceIdx]
            newState[self.emptySpaceIdx] = temp
            # create the child
            self.children.append(puzzleNode(newState, self, 'D'))
    
    # function to get the nodes state
    def getState(self):
        return self.theBoardState

    # function to get the left child
    def getChildren(self):
        self.getLeftMove()
        self.getRightMove()
        self.getUpMove()
        self.getDownMove()
        return self.children
    


def bfs(initialNode, endState):
    frontier = Queue()
    frontier.put_nowait(initialNode)
    explored = set()
    while not frontier.empty():
        state = frontier.get_nowait()
        children = state.getChildren()
        
        for i in range(len(children)):
            childState = children[i].getState()
            if childState == endState:
                return children[i]
            if children[i] not in explored:
                explored.add(children[i])
                frontier.put_nowait(children[i])
    return "Failed"


def main():
    board = [int(square) for square in input().split()]
    root = puzzleNode(board, None, None)
    solved = bfs(root, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0])    

if __name__ == '__main__':
    main()