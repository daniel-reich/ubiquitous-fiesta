
def trace_word_path(word, grid):
​
    def search(w, path):
        cr, cc = path[-1]
        # check all cells neighbouring last match in path
        for nr, nc in [(cr+1, cc), (cr, cc+1), (cr-1,cc), (cr, cc-1)]:
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == w[0] and not (nr, nc) in path:
                # found next letter @(nr, nc), append coordinates to path
                path.append((nr, nc))
                # last letter found return `done` flag
                if len(w) == 1: return True
                # recurse for remainder of word
                if search(w[1:], path): 
                    # successful search complete - return final path
                    return path
                else:
                    # unsuccessful search, remove last coord and try next candidate
                    path.pop();
        # no unvisited neighbours match next letter
        return False
    
    # find possible starting points
    for r,c in [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == word[0]]:
        # recursive search for path to remeinder of word
        path = search(word[1:], [(r, c)])
        if path:
            return path
    return 'Not present'

