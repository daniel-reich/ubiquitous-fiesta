
def largest_island(lst):
    visited = set()
    def check(rows, cols):
        if not (0 <= rows < len(lst) and 0 <= cols < len(lst[0]) and (rows, cols) not in visited and lst[rows][cols]):
            return 0
        visited.add((rows, cols))
        return (1 + check(rows+1, cols) + check(rows-1, cols) + check(rows, cols-1) + check(rows, cols+1) + check(rows-1,cols-1) + check(rows+1,cols+1) + check(rows+1,cols-1) + check(rows-1,cols+1))
​
    return max(check(rows, cols)
                for rows in range(len(lst))
                for cols in range(len(lst[0])))

