from __future__ import print_function
import random
import sys


class player:

    MAX_DEPTH = 8;
 
    WIN_REV = 1;
    LOSE_REV = -1;
    IDK_REV = 0;
    
    def __init__(self, playername, playernum):
        self.playername = playername
        self.playernum = playernum
        print("test")

    def getname(self):
        return self.playername

    #board[2][3] = row 3, col 3
    
    def requestmovement(self, board, height):
        fakeBoard = board
        move = 0
        maxValue = -1 * sys.maxsize

        for x in range(7):   
            colcount[x] = self.getColCount(fakeBoard, x)

        for col in range(7):
            if (self.isValidMove(fakeBoard, col)):
                value = moveValue(col, fakeBoard);
                if (value > maxValue):
                    maxValue = value
                    if (value == WIN_REV):
                        break


        return col;

    ## NOTE(DANIEL): Don't think this is right
    def getColCount(self, fakeBoard, col):
        count = 0
        for col in range(7):
            for row in range(6):
                if (fakeBoard[col][row] in [1,2]):
                    count += 1
        return count

    def isValidMove(self, fakeBoard, col):
        return self.getColCount(fakeBoard, col) < 7 

    def makeMove(self, fakeBoard, col, me):
        colcount = self.getColCount(fakeBoard, col)
        if (count < height):
            if (me):
                sign = self.playernum
            else:
                if (self.playernum == 1):
                    sign = 2
                elif (self.playernum == 2):
                    sign = 1

            fakeBoard[col][colcount] = sign
            return True
        else:
            return False

    def undoMove(self, fakeBoard, col, me):
        colcount = self.getColCount(fakeBoard, col)
        if (colcount > 0):
            if (me):
                sign = self.playernum
            else:
                if (self.playernum == 1):
                    sign = 2
                elif (self.playernum == 2):
                    sign = 1
            if (fakeBoard[col][colcount - 1] == sign):
                fakeBoard[col][colcount - 1] = 0
                return True
        return False


def main():
    # 7 x 6
    p = player("Dan", 1)
    fboard = [[1,1,1,1,2,2],
              [0,0,0,0,0,0],
              [0,0,0,0,0,0],     ## This is North for board
              [0,0,0,0,0,0],
              [0,0,0,0,0,0],
              [0,0,0,0,0,0],
              [0,0,0,0,0,0]]
    printBoard(fboard)
    print(p.isValidMove(fboard, 0))

def printBoard(board):
    for row in range(-1, -7, -1):
        if (row == -6):
            row = 0
        for col in range(7):
           print(board[col][row], end='')

        print()

if __name__ == "__main__":
    main()
   
