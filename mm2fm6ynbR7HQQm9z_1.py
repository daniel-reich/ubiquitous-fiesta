
deltas = [[1, 2], [1, -2], [-1, 2], [-1, -2],
          [2, 1], [2, -1], [-2, 1], [-2, -1]]
​
def knights_jump(square):
    row, col = ord(square[0]) - 65, int(square[1]) - 1
    ans = []
    for col2 in range(8):
        for row2 in range(8):
            if sorted([abs(row - row2), abs(col - col2)]) == [1, 2]:
                ans.append(chr(65+row2) + str(1+col2))
    return ','.join(ans)

