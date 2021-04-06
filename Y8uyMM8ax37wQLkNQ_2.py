
# re-use solution from "Primes Spiral":
def matrix(n):
    primes = list(range(1, n**2 + 1))
    M = [[0 for row in range(n)] for col in range(n)]
    directions = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    pos = 0
    row, col = 0, 0
    direction = 0
    while pos < n**2 - 1:
        M[row][col] = primes[pos]
        nxt_row, nxt_col = row + directions[direction][0], col + directions[direction][1]
        while nxt_row < 0 or nxt_row == n or nxt_col < 0 or nxt_col == n or \
              M[nxt_row][nxt_col] != 0:
            direction = (direction + 1) % 4
            nxt_row, nxt_col = row + directions[direction][0], col + directions[direction][1]
        row, col = nxt_row, nxt_col
        pos += 1
    M[row][col] = primes[-1]
    return M

