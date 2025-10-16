import copy

from Problem_Class import TicTacToeProblem
MEMO = {}
""" at each level, search will determine whos turn it is and get all the successors at that level. it will 
Then weight each path and choose the max of the minimum values path. ie: if the successors """
def endState(state):
    boardState = copy.deepcopy(state[0])
    rowOne = boardState[0]
    rowTwo = boardState[1]
    rowThree = boardState[2]
    
    # row O wins
    if (rowOne == ['O','O','O']) or (rowTwo == ['O','O','O']) or rowThree == ['O','O','O']:
        return (True, -1)
    # row X wins
    elif rowOne == ['X','X','X'] or rowTwo == ['X','X','X'] or rowThree == ['X','X','X']:
        return (True, 1)
    #collum X and O wins
    for i in range(3):
        if rowOne[i] == 'X' and rowTwo[i] == 'X' and rowThree[i] == 'X':
            return (True, 1)
        if rowOne[i] == 'O' and rowTwo[i] == 'O' and rowThree[i] == 'O':
            return (True, -1)
    # diagonal X wins
    if rowOne[0] == 'X' and rowTwo[1] == 'X' and rowThree[2] == 'X':
        return(True, 1)
    if rowOne[2] == 'X' and rowTwo[1] == 'X' and rowThree[0] == 'X':
        return(True, 1)
    # diagonal O wins
    if rowOne[0] == 'O' and rowTwo[1] == 'O' and rowThree[2] == 'O':
        return(True, -1)
    if rowOne[2] == 'O' and rowTwo[1] == 'O' and rowThree[0] == 'O':
        return(True, -1)
    # handling for if its not a finished board state, ie: there are still empty squares, in which it will
    # return False, as it is not an end State
    for i in range(3):
        for j in range(3):
            if boardState[i][j] == None:
                return (False, 0)

    return (True, 0)

# print(endState([[['O','X','O'],['X','O',None],['O',None,'O']],'X']))
class Node:
    def __init__(self,state):
        self.state = state
        childStates = []
        parentNode = None
        
def stateToString(state):
    player = state[-1]
    board = state[0]
    stringBuilder = ''
    for i in range(3):
        for s in range(3):
            stringBuilder += str(board[i][s])
    # stringBuilder += player
    return stringBuilder

def MinMaxSearch(state):
    global MEMO
    if stateToString(state) in MEMO:
        return MEMO[stateToString(state)]
    player = state[-1]
    
    
    (end,score) = endState(state)
    if end:
        key = stateToString(state)
        MEMO[key] = (score,state)
        return (score,state)
    else:
        ttt = TicTacToeProblem(state)
        successors = ttt.getSuccessors(state)
        if player == 'X':
            bestScore = -10
            for childState in successors:
                childScore = MinMaxSearch(childState)
                # print(childScore)
                if childScore[0] > bestScore:
                    bestScore = childScore[0]
                    bestChild = childState
                # bestScore = max(bestScore, childScore[0])
                
            key = stateToString(state)
            MEMO[key] = (bestScore,bestChild)
            
            return (bestScore, bestChild)
        if player == 'O':
            bestScore = 10
            for childState in successors:
                childScore = MinMaxSearch(childState)
                # print(childScore)
                if childScore[0] < bestScore:
                    bestScore = childScore[0]
                    bestChild = childState
            key = stateToString(state)
            MEMO[key] = (bestScore,bestChild)
            
            
            return (bestScore, bestChild)



   

# retval = MinMaxSearch(
#     [[['X',None,'O'],
#       ['O','X',None],
#       [None,None,None]],
#       # player who is going in this state:
#       'X'])
# print(retval)
# print(stateToString([
#       [['X','X','O'],
#       ['X','X','O'],
#       ['X','O',None]],
#       'X']))
