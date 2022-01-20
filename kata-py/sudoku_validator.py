from itertools import chain
def valid_solution(board):
    result = True
    for row in board:
        for column in row:
            if column == 0:
                result = False
            if row.count(column) != 1:
                result = False
    board_transpose = [*zip(*board)]
    for row in board_transpose:
        for column in row:
            if row.count(column) != 1:
                result = False
    board_square = [list(chain.from_iterable([board[0][0:3], board[1][0:3], board[2][0:3]])),
                    list(chain.from_iterable([board[3][0:3], board[4][0:3], board[5][0:3]])),
                    list(chain.from_iterable([board[6][0:3], board[7][0:3], board[8][0:3]])),
                    list(chain.from_iterable([board[0][3:6], board[1][3:6], board[2][3:6]])),
                    list(chain.from_iterable([board[3][3:6], board[4][3:6], board[5][3:6]])),
                    list(chain.from_iterable([board[6][3:6], board[7][3:6], board[8][3:6]])),
                    list(chain.from_iterable([board[0][6:9], board[1][6:9], board[2][6:9]])),
                    list(chain.from_iterable([board[3][6:9], board[4][6:9], board[5][6:9]])),
                    list(chain.from_iterable([board[6][6:9], board[7][6:9], board[8][6:9]]))]
    for row in board_square:
        for column in row:
            if row.count(column) != 1:
                result = False
    return result

m1 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2, 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9]]

m2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 0, 3, 4, 9],
      [1, 0, 0, 3, 4, 2, 5, 6, 0],
      [8, 5, 9, 7, 6, 1, 0, 2, 0],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 0, 1, 5, 3, 7, 2, 1, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 0, 0, 4, 8, 1, 1, 7, 9]]

m3 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [2, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2 , 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9]]

print(valid_solution(m3))

### Test ###
# def transpose(m):
#     t_matrix = [*zip(*m)]
#     return t_matrix
# print(transpose(m3))

# m3t = [*zip(*m3)]
# print(m3t)
# list = [[1],[2],[3]]