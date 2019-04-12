class Queen:
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def getRow(self):
        return self._row
    
    def getColumn(self):
        return self._column
    
    def canAttack(self, queen):
        canAttackVertically   = (self._column == queen._column)
        canAttackHorizontally = (self._row == queen._row)
        canAttackDiagonally   = (self._row - queen._row == self._column - queen._column)

        return canAttackVertically or canAttackHorizontally or canAttackDiagonally

class NQueens:
    def __init__(self, n = 8):
        self._size = n
        self._queens = []

    def contains(self, row, column):
        for queen in self._queens:
            if queen.getRow() == row and queen.getColumn() == column:
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
    
