from SudokuSolver import SudokuSolver
from ImageDigitReader import ImageDigitReader


class Main:
    image = ImageDigitReader()

    sudoku_board_img = image.get_sudoku_board()

    sudoku_board = [
        [4, 1, 7, 0, 0, 0, 5, 0, 0],
        [5, 0, 0, 0, 6, 0, 4, 2, 0],
        [0, 6, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 3, 7, 0],
        [1, 5, 3, 0, 7, 2, 0, 8, 0],
        [0, 0, 0, 3, 0, 8, 6, 0, 0],
        [9, 2, 8, 7, 0, 0, 1, 4, 3],
        [0, 0, 5, 0, 9, 0, 8, 0, 0],
        [6, 0, 1, 4, 0, 0, 2, 9, 5]
    ]
    sudoku = SudokuSolver(sudoku_board_img)

    sudoku.print_solved_sudoku()
