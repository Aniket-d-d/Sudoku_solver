def solve(board):
    find = find_null_place(board)

    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if validate(board, num, row, col):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def validate(board, num, row, col):
    for i in range(9):
        if board[row][i] == num:
            return False

    for j in range(9):
        if board[j][col] == num:
            return False

    ro = col // 3
    co = row // 3

    for i in range(co * 3, co * 3 + 3):
        for j in range(ro * 3, ro * 3 + 3):
            if board[i][j] == num:
                return False

    return True


def find_null_place(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


"""
for _ in matrix:
    print(_)
solve(matrix)
print()
for _ in matrix:
    print(_)

"""
