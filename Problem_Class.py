import copy
class TicTacToeProblem:
    def __init__(self,  initState):
        """ arbitrary state:
        [[(None,None,None),(None,None,None),(None,None,None)],'X']
        each rows value, and the starting player"""
        
        self.initState = initState
    def getSuccessors(self, state):
        # retval will hold all of the possible successors.
        retval = []
        # newBoard will hold the new version of the board that we are creating at 
        # each None that is found.
        newBoard = []
        boardState = copy.copy(state[0])
        currPlayer = state[1]
        # given the current player, storing the next player to append
        # to all the successor states.
        if currPlayer == 'X':
            nextPlayer = 'O'
        else:
            nextPlayer = 'X'
        # two loops looping for three each, to iterate through each element in
        # each row.
        for i in range(3):
            for j in range(3): 
                # if the space is empty (none), then copy the boardstate into the newBoard 
                # so we can start building what the successor will look like without overwriting any data.    
                if boardState[i][j] == None:
                    newBoard = copy.deepcopy(boardState)
                    # changing the empty spot that has been found to hold the player, and keeping 
                    # the rest of the board state the same
                    newBoard[i][j] = currPlayer
                    # adding the next player to the end
                    newState = []
                    newState.append(newBoard)
                    newState.append(nextPlayer)
                    
                    # adding the current state to retval, which will return a list of all the found states.
                    retval.append(newState)
        return retval
    

# ttt = TicTacToeProblem([[[None,None,None],[None,None,None],[None,None,None]],'X'])
# foundStates = ttt.getSuccessors([[[None,None,None],[None,None,None],[None,None,None]],'X'])
# print(foundStates)
        
            


            

