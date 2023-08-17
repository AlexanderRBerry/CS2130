class Nqueens:
    def __init__(self, n):
        self.n = n
        self.queens = [-1] * n

    def print_solution(self):
        """Print the board using the positioning found in the
        queens array.  If queens[0] = -1 you should print "No solution"
        When printing the board use "|" to separate columns and
        new lines to separate rows.  Mark queens with a "Q" and empty
        squares with a  ' ' """
        if self.queens[0] == -1:
            print("No solution")
            return
        boardString = ""
        for row in range(len(self.queens)):
            numSpaces = 0
            for column in range(len(self.queens)):
                if numSpaces == self.queens[row]:
                    boardString += "|Q"
                else:
                    boardString += "| "
                numSpaces += 1
            boardString += "|\n"
        print(boardString)

    def is_valid(self, rows):
        """Check if the positioning listed in the queens arrays is valid up to "rows"
        Ignore queens with an index >= rows.
        A valid position is one which does not share a column or diagonal with
        any other queen."""
        isValid = True
        # Verifying that no queens share the same column
        for i in range(rows):
            if self.queens[i] in self.queens[i+1:rows] or self.queens[i] in self.queens[:i]:
                isValid = False
                break
            # Verifying that no queens share a diagonal
            for j in range(i+1, rows):
                if i == j:  # To prevent a queen from being compared to itself
                    continue
                if ((i + self.queens[i]) == (j + self.queens[j]) or
                        (i - self.queens[i]) == (j - self.queens[j])):
                    isValid = False
        return isValid

    def backtrack(self, row):
        if row == self.n:
            return self.is_valid(row)

        for col in range(self.n):
            self.queens[row] = col
            if self.is_valid(row + 1) and self.backtrack(row + 1):
                return True
            self.queens[row] = -1

        return False

    def backtracking_find_solution(self):
        self.backtrack(0)

    def bruteforce(self, row):
        if row == self.n:
            return self.is_valid(row)

        for col in range(self.n):
            self.queens[row] = col
            if self.bruteforce(row + 1):
                return True
            self.queens[row] = -1

        return False

    def brute_force_find_solution(self):
        self.bruteforce(0)