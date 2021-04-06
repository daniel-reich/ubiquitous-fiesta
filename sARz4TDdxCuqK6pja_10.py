
import copy
​
def spread_virus(persons):
    new_persons = copy.deepcopy(persons)
    h, w = len(persons), len(persons[0])
    for r in range(h):
        for c in range(w):
            if persons[r][c] == "V":
                for r2, c2 in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= r2 < h and 0 <= c2 < w:
                        new_persons[r2][c2] = "V"
    return new_persons
    
def deadly_virus(persons, n):
    for _ in range(n):
        persons = spread_virus(persons)
    return persons

