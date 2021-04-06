
def word_search(letters, words):
    safe = []
    grid = [list(letters[x:x+8]) for x in range(0, 64, 8)]
    for x in words:
        x = x.upper()
        if x in letters or x[::-1] in letters:
            safe.append(True)
            continue
        for row in range(8):
            for col in range(8):
                if grid[row][col] == x[0]:
                    d = row + len(x) - 1 < 8
                    u =  row - len(x) >= -1
                    if d:
                        c = ''.join([grid[row+d][col] for d in range(len(x))])
                        if c == x or c[::-1] == x:
                            safe.append(True)
                    if u:
                        c = ''.join([grid[row-d][col] for d in range(len(x))])
                        if c == x or c[::-1] == x:
                            safe.append(True)
                            
​
                    if row + len(x) < 8 and col - len(x) >= -1:
                        c = ''.join(grid[row+d][col-d] for d in range(len(x)))
                        if c == x or c[::-1] == x:
                            safe.append(True)
                    
                    if row + len(x) < 8 and col + len(x) <= 8:
                        c = ''.join(grid[row+d][col+d] for d in range(len(x)))
                        if c == x or c[::-1] == x:
                            safe.append(True)
​
                    if u and col + len(x) <= 8:
                        c = ''.join(grid[row-d][col+d] for d in range(len(x)))
                        if c == x or c[::-1] == x or c in words or c[::-1] in words:
                            safe.append(True)
                    
                    if u and col - len(x) >= -1:
                        c = ''.join(grid[row-d][col-d] for d in range(len(x)))
                        if c == x or c[::-1] == x or c[::-1] in words:
                            safe.append(True)
​
    return len(safe) == len(words)

