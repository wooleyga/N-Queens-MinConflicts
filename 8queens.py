class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def canAttack(self, row, column):
        canAttackVertically   = (self.column == column)
        canAttackHorizontally = (self.row == row)
        canAttackDiagonally   = (self.row - row == self.column - column)

        return canAttackVertically or canAttackHorizontally or canAttackDiagonally

class NQueens:
    def __init__(self, n = 8):
        self._size = n
        self._queens = []

    def contains(self, row, column):
        for queen in self._queens:
            if queen.row == row and queen.column == column:
                return True
        return False

    def isFull(self):
        return len(self._queens) == self._size

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
                if self._queens[i].canAttack(self._queens[j]):
                    return False
        return True

