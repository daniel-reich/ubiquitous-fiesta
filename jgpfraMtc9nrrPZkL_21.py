
def switch_gravity_on(grid):
    number_of_obj = [0 for _ in range(len(grid[0]))]
    new_grid = [['-' for col in range(len(grid[row]))] for row in range(len(grid))]
​
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                number_of_obj[col] += 1
    
    for row in reversed(range(len(grid))):
        for col in range(len(grid[row])):
            if number_of_obj[col] > 0:
                new_grid[row][col] = '#'
                number_of_obj[col] -= 1
​
    return new_grid

