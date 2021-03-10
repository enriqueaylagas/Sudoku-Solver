import cv2
import pytesseract


class ImageDigitReader:
    board_nums = []
    sudoku_board = []
    pytesseract.pytesseract.tesseract_cmd = '/Users/enriqueaylagas/PycharmProjects/SudokuSolver/tesseract'
    img = cv2.imread('sudoku6.png')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(pytesseract.image_to_string(img))

    hImg, wImg, _ = img.shape
    cong = r' --oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_boxes(img, config=cong)

    for b in boxes.splitlines():
        # print(b)
        b = b.split(' ')
        # print(b[0])
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        digit = int(b[0])

        if len(board_nums) < 9:
            board_nums.append(digit)



        else:

            sudoku_board.append(board_nums)
            board_nums = []
            board_nums.append(digit)


        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 2)
        cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50255), 2)
    sudoku_board.append(board_nums)
    print(sudoku_board)

    #cv2.imshow('Result', img)
    #cv2.waitKey(0)

    def get_sudoku_board(self):
        return self.sudoku_board
