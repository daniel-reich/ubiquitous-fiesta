
def perfect_cut(carat):
    diamond = [[0 for _ in range(carat)] for __ in range(carat)]
    mid = carat // 2
    for row in range(carat // 2 + 1):
        diamond[row][mid - row] = 1
        diamond[row][mid + row] = 1
        diamond[carat - 1 - row][mid - row] = 1
        diamond[carat - 1 - row][mid + row] = 1
    return [diamond, 'perfect cut']
​
def good_cut(carat):
    diamond = [[0 for _ in range(carat)] for __ in range(carat - 1)]
    mid = carat // 2
    for row in range(carat // 2):
        diamond[row][mid - row - 1] = 1
        diamond[row][mid + row] = 1
        diamond[carat - 2 - row][mid - row - 1] = 1
        diamond[carat - 2 - row][mid + row] = 1
    return [diamond, 'good cut']
    
def diamond(carat):
    return good_cut(carat) if carat % 2 == 0 else perfect_cut(carat)

