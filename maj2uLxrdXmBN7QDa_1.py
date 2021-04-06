
deltas = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
​
def get_row_col(sq):
    return (ord(sq[0]) - 97, int(sq[1]) - 1)
​
def bishop(start, end, n):
    if start == end:
        return True
    if n == 0:
        return False
    start = get_row_col(start)
    end = get_row_col(end)
    dist = {start: 0}
    queue = [start]
    while len(queue) > 0:
        (row, col) = queue.pop(0)
        for drow, dcol in deltas:
            row2, col2 = row + drow, col + dcol
            while 0 <= row2 <= 7 and 0 <= col2 <= 7:
                if (row2, col2) not in dist:
                    dist[(row2, col2)] = dist[(row, col)] + 1
                    queue.append((row2, col2))
                    if (row2, col2) == end:
                        return dist[(row2, col2)] <= n
                row2, col2 = row2 + drow, col2 + dcol
    return False

