class SudokuSolver:

    def __init__(self, board):

        self.board = board

    def print_board(self):
        """ Prints the current board to solve"""

        for i in range(len(self.board)):

            if i % 3 == 0 and i != 0:
                print("------------------------")
            for j in range(len(self.board[0])):

                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])

                else:
                    print(str(self.board[i][j]) + " ", end="")

    def find_empty_space(self):
        """ Looks through board and finds a place that holds no number or '0' """

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):

                if self.board[i][j] == 0:
                    return i, j

    def potential_num(self, num, position):
        """ Checks if the number we are putting in the board is potentially correct"""

        # Checking if number appears in row
        for i in range(len(self.board[0])):
            if self.board[position[0]][i] == num and position[1] != i:
                return False

        # Checking if number appears in column
        for i in range(len(self.board)):
            if self.board[i][position[1]] == num and position[0] != i:
                return False

        # Checking if number appears in 3 x 3 box
        x = position[1] // 3  # column given by 'find_empty_space' integer divided by 3 since boxes are 3x3
        y = position[0] // 3  # row given by 'find_empty_space' integer divided by 3 since boxes are 3x3

        for i in range(y * 3, y * 3 + 3):
            for j in range(x * 3, x * 3 + 3):
                if self.board[i][j] == num and (i, j) != position:
                    return False
        return True

    def solve_sudoku(self):
        """ Puts in Number after checking if it is potentially correct, if next number does not have valid number,
         it makes previous number check again until it gets to the last number in the board"""

        empty = self.find_empty_space()

        if not empty:
            return True

        else:
            row, column = empty

        for i in range(1, 10):

            if self.potential_num( i, (row, column)):
                self.board[row][column] = i

                if self.solve_sudoku():
                    return True

                self.board[row][column] = 0

        return False

    def print_solved_sudoku(self):
        """ Prints out whole Process"""
        print("Sudoku Board to Solve:\n")
        self.print_board()
        print()
        self.solve_sudoku()
        print("Solved Board:\n")
        self.print_board()
