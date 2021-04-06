
from collections import defaultdict
​
def trace_word_path(word, grid):
    global matrix
    global steps
    matrix = defaultdict(lambda: " ")
    steps = [(-1,0),(0,-1),(0,1),(1,0)]
​
    cells = {(i,j) : char for i, line in enumerate(grid) for j, char in enumerate(line)}
    imax = max([coord[0] for coord in cells.keys()])
    jmax = max([coord[1] for coord in cells.keys()])
    for coord in cells.keys():
        matrix[coord] = cells[coord]  
    for start in [coord for coord, val in matrix.items() if val == word[0]]:
        chemin = [start]
        res = next_letter(chemin, word[1:])
        if res == False:
            chemin = chemin[:-1]
        else:
            return res
    return "Not present" 
​
def next_letter(chemin, word):
    global matrix
    global steps
    print (chemin, word)
    if word == "":
        return chemin
    start = chemin[-1]
    for step in steps:
        coord = (start[0]+step[0], start[1]+step[1])
        if matrix[coord] == word[0] and coord not in chemin:
            chemin.append(coord)
            res = next_letter(chemin, word[1:])
            if res == False:
                chemin = chemin[:-1]
            else:
                return res
    return False
​
​
print(trace_word_path("UKULELE", [
  ['N', 'H', 'B', 'W'], 
  ['E', 'X', 'A', 'D'], 
  ['L', 'A', 'U', 'U'], 
  ['E', 'L', 'U', 'K']
]))
print([(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2)])

