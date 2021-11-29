# Functions used to solve the sudoku puzzle

def row_solid(board: list) -> list:
    result = []
    for i in range(len(board)):
        temp = []
        for j in range(len(board)):
            if board[i][j]:
                temp.append(board[i][j])
        result.append(temp)
    return result


def col_solid(board: list) -> list:
    result = []
    for i in range(len(board)):
        temp = []
        for j in range(len(board)):
            if board[j][i]:
                temp.append(board[j][i])
        result.append(temp)
    return result


def box_solid(board: list) -> list:
    result = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if board[k][l]:
                        temp.append(board[k][l])
            result.append(temp)
    return result

