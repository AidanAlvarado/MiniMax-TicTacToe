import Problem_Class
from MinMax_search import MinMaxSearch
from MinMax_search import endState
import sys


class Game:
    # this holds the initial board state and all the proceeding board states.
    def __init__(self):
        self.boardState = [
            [[None, None, None], [None, None, None], [None, None, None]],
            "X",
        ]

    # play is called to initiate the game. it recurses and refreshes the board state and keeps track of the player.
    def play(self, turn="X"):

        if turn == "X":
            print("X's Turn:")
            print("X thinking...")
            score, newBoard = MinMaxSearch(self.boardState)
            self.boardState = newBoard

            self.render(self.boardState)
            isWin, score = endState(self.boardState)
            if isWin:
                self.end(score)
            else:
                self.play("O")
        elif turn == "O":
            print("O's Turn:")

            playerRow = int(input("What row would you like to play: "))
            playerColumn = int(input("What column would you like to play: "))

            # handling for nonsense inputs from user

            if not playerRow >= 0 and not playerRow <= 2:
                print("sorry - that row is out of range. ")
                self.play("O")
            elif not playerColumn >= 0 and not playerColumn <= 2:
                print("sorry - that column is out of range. ")
                self.play("O")

            if self.boardState[0][playerRow][playerColumn] != None:
                print("sorry - cant play in occupied squares.")
                self.play("O")

            self.boardState[0][playerRow][playerColumn] = "O"
            self.boardState[-1] = "X"
            self.render(self.boardState)
            isWin, score = endState(self.boardState)
            if isWin:
                self.end(score)
            else:
                self.play("X")

    def render(self, state):
        # goes thru each cell in the state and  s its value and writes bars between.
        for i in range(3):
            for j in range(3):
                if state[0][i][j] != None:
                    print(state[0][i][j], end="")
                    if j <= 1:
                        print(" | ", end="")
                else:
                    print("-", end="")
                    if j <= 1:
                        print(" | ", end="")
            print()

        # print(state[-1],end='')
        # print('s turn.')

    def end(self, score):
        # prints the winner
        if score == -1:
            print("O wins!")
            sys.exit()
        elif score == 1:
            print("X wins!")
            sys.exit()
        else:
            print("Tied!")
            sys.exit()


g = Game()
g.play()
