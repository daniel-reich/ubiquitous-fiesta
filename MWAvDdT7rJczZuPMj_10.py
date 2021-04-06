
def count_word(grid, word):
    lst,count = [[False for j in i] for i in grid],[]
    maxr,maxc = len(grid),len(grid[0])
    def helper(row,col,word,move=(0,0)):
        valid = False
        if len(word) == 1:
            count.append(1)
            valid = True
        else:
            for direction in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                r,c = row+direction[0],col+direction[1]
                if 0 <= r < maxr and 0 <= c < maxc:
                    if grid[r][c] == word[1] and (move == (0,0) or move == direction):
                        if helper(r,c,word[1:],direction):
                            valid = True
        if valid:
            lst[row][col] = True
            return True
        return False
​
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == word[0]:
                helper(i,j,word)
    return len(count),[[j.lower() if lst[index_r][index_c] else j for index_c,j in enumerate(i)] for index_r,i in enumerate(grid)]

