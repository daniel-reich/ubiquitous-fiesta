
def darts_solver(sections, darts, target):
    '''Returns a sorted list of unique sorted solutions as strings delimited with '-'
    Throwing a certain amount of valid darts, find how many solutions there are to reach the target score.
    Sections: A list of values for the sections (e.g. [3, 6, 8], the list is already sorted).
    Darts: The amount of darts to throw.
    Target: The target score.'''
​
    sum_throws = lambda: sum([sections[x] for x in throws])
    n_sections = len(sections)
    solutions = []
    throws = [0] * darts
    throws[0] = -1
    i = 0
    while i < darts:
        throws[0] += 1
        if throws[0] < n_sections:
            if sum_throws() == target:
                lst = sorted([sections[x] for x in throws])   
                if not lst in solutions:
                    solutions.append(lst)
        else:
            i = 0
            while throws[i] == n_sections or sum_throws() > target:
                throws[i] = 0
                i += 1
                if i == darts: break
                throws[i] += 1
    
    out = []
    for q in sorted(solutions):
        out.append('-'.join([str(x) for x in q]))  
    return out

