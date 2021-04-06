
def game_of_life(board):
    output = []
    for i, row in enumerate(board):
        for t, element in enumerate(row):
            neighbours = get_neighbours(t, i, board)
            output.append(get_output(element, neighbours))
        output.append('\n')
    return ''.join(output[:-1])
​
def get_neighbours(element_idx, row_idx, board):
    neighbours = []
    if row_idx > 0:
        neighbours.append(board[row_idx - 1][element_idx])
        if element_idx > 0:
            neighbours.append(board[row_idx - 1][element_idx - 1])
        if element_idx < len(board[row_idx]) - 1:
            neighbours.append(board[row_idx -1][element_idx + 1])
    if row_idx < len(board) - 1:
        neighbours.append(board[row_idx + 1][element_idx])
        if element_idx > 0:
            neighbours.append(board[row_idx + 1][element_idx - 1])
        if element_idx < len(board[row_idx]) - 1:
            neighbours.append(board[row_idx + 1][element_idx + 1])
​
    if element_idx > 0:
        neighbours.append(board[row_idx][element_idx - 1])
    if element_idx < len(board[row_idx]) - 1:
        neighbours.append(board[row_idx][element_idx + 1])
    return neighbours
​
​
def get_output(element, neighbours):
    ones = neighbours.count(1)
​
    if element:
        if ones in [2, 3]:
            return 'I'
        else:
            return '_'
​
    elif not element:
        if ones == 3:
            return 'I'
        else:
            return '_'

