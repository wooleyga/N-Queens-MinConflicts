import random
import sys

class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def canAttack(self, row, column):
        canAttackVertically   = (self.column == column)
        canAttackHorizontally = (self.row == row)
        canAttackDiagonally   = (abs(self.row - row) == abs(self.column - column))

        return canAttackVertically or canAttackHorizontally or canAttackDiagonally

class NQueens:
    def __init__(self, n = 8):
        self._size = n
        self._queens = []
    
    def __str__(self):
        tostring = ""
        for i in range(self._size):
            for j in range(self._size):
                if (self.contains(i, j)):
                    tostring += "x"
                else:
                    tostring += "-"
            tostring += "\n"
        return tostring

    def getSize(self):
        return self._size

    def getQueens(self):
        return self._queens

    def contains(self, row, column):
        for queen in self._queens:
            if queen.row == row and queen.column == column:
                return True
        return False

    # Returns True if the board is full of queens, False otherwise
    def isFull(self):
        return len(self._queens) == self._size

    # Returns True if the position is valid (in the board space), False otherwise
    def _isInvalidPosition(self, row, column):
        return row >= self._size or column >= self._size
    
    # Adds a Queen to the board
    # Returns True if added, False if a Queen cannot be added (already exists or invalid request)
    def addQueen(self, row, column):
        if self.contains(row, column) or self.isFull() or self._isInvalidPosition(row, column):
            return False
        else:
            self._queens.append(Queen(row, column))
            return True

    # Returns the number of conflicts at the position (row, column)
    def getNumberOfConflicts(self, row, column):
        numberOfConflicts = 0
        for queen in self._queens:
            if queen.canAttack(row, column):
                numberOfConflicts += 1
        return numberOfConflicts
    
    # Moves a Queen from the position (originalRow, originalColumn) to the new position (newRow, newColumn)
    # Returns True if the change was made, False otherwise
    def moveQueen(self, originalRow, originalColumn, newRow, newColumn):
        if not self.contains(originalRow, originalColumn) or self.contains(newRow, newColumn):
            return False
        else:
            for queen in self._queens:
                if queen.row == originalRow and queen.column == originalColumn:
                    queen.row    = newRow
                    queen.column = newColumn
                    return True
    
    # Returns if the solution is valid (ie. no queens conflict)
    def isValid(self):
        for i in range(len(self._queens) - 1):
            for j in range(i + 1, len(self._queens)):
                if self._queens[i].canAttack(self._queens[j].row, self._queens[j].column):
                    return False
        return True

# Fills the nQueens with Queens until it is full (conflicts not considered)
def fillNQueens(nQueens):
    for row in range(nQueens.getSize()):
            for column in range(nQueens.getSize()):
                if not nQueens.isFull():
                    nQueens.addQueen(row, column)
                else:
                    return

# Returns the minimum number of conflicts for nQueens in a column (ignoring rowToIgnore)
def minNumberOfConflicts(nQueens, rowToIgnore, column):
    mini = sys.maxsize
    for row in range(nQueens.getSize()):
        if row != rowToIgnore and nQueens.getNumberOfConflicts(row, column) < mini:
            mini = nQueens.getNumberOfConflicts(row, column)
    return mini

# Performs min-conflicts to make nQueens valid
# Returns the number of steps needed to complete
def minConflicts(nQueens):
    if not nQueens.isFull():
        fillNQueens(nQueens)
    
    steps = 0
    while not nQueens.isValid():
        # Find a randomly chosen queen that has a conflict
        conflicts = [queen for queen in nQueens.getQueens() if nQueens.getNumberOfConflicts(queen.row, queen.column) > 0]

        randomIndex = random.randint(0, len(conflicts) - 1)
        queenToMove = conflicts[randomIndex]

        # Find the space to move the queen to that has the minimum amount of conflicts (random if multiple spaces)
        rowsToMove = [row for row in range(nQueens.getSize()) if row != queenToMove.row]
        minPossibleConflict = minNumberOfConflicts(nQueens, queenToMove.row, queenToMove.column)
        possibleMoves = [row for row in rowsToMove if nQueens.getNumberOfConflicts(row, queenToMove.column) == minPossibleConflict]
        
        randomIndex = random.randint(0, len(possibleMoves) - 1)
        newRow = possibleMoves[randomIndex]

        # Move Queen
        nQueens.moveQueen(queenToMove.row, queenToMove.column, newRow, queenToMove.column)
        
        steps += 1

    return steps

nQueens = NQueens()
steps = minConflicts(nQueens)
print(nQueens)
print("Steps: " + str(steps))
