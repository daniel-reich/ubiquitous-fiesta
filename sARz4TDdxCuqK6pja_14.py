
def deadly_virus(pop, t):
    '''
    Returns a copy of pop updated for the spread of the virus after t hours
    '''
    HEIGHT = len(pop)
    WIDTH = len(pop[0])
​
    def is_infected(pop, i, j):
        '''
        Returns whether the person at pop[i][j] is infected or has an infected
        neighbour who therefore infects them.
        '''
        persons = ((i-1,j),(i+1,j),(i,j),(i,j-1),(i,j+1))
​
        return any(pop[r][c] == 'V' for r,c in persons
                   if 0<=r<HEIGHT and 0<=c<WIDTH)
​
    for _ in range(t):
        new_pop = [['V' if is_infected(pop,i,j) else 'P'
                    for j in range(WIDTH)]
                    for i in range(HEIGHT)]
        pop = new_pop
        
    return pop

