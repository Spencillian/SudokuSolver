# Functions used to check over the sudoku puzzle

def eval_rows(board: list) -> bool:
    for row in board:
        temp = [i for i in range(1, 10)]
        for num in row:
            if num in temp:
                temp.remove(num)
        if temp:
            return False
    return True


def eval_cols(board: list) -> bool:
    for i in range(len(board)):
        temp = [i for i in range(1, 10)]
        for row in board:
            if row[i] in temp:
                temp.remove(row[i])
        if temp:
            return False
    return True


def eval_box(board: list) -> bool:
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = [i for i in range(1, 10)]
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if board[k][l] in temp:
                        temp.remove(board[k][l])
            if temp:
                return False
    return True


def check(board: list) -> bool:
    return eval_rows(board) and eval_cols(board) and eval_box(board)
