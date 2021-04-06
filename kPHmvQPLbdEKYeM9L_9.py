
def asteroid_collision(asteroids):
    '''
    Returns asteroids with any exploded ones removed, as per instructions.
    '''
    def winner(ast, rights):
        '''
        Returns True if ast survives collision with rights and updates
        rights appropriately
        '''
        for i in range(len(rights)-1, -1, -1):
            if ast > rights[i]:
                del rights[i]  # left moving asteroid destroyed this one
            elif ast == rights[i]:
                del rights[i]
                return False   # both destroyed
            else:
                return False   # ast destroyed
​
        return True  # ast survived
            
    rights, survivors = [], []
    for ast in asteroids:
        if ast < 0:
            if winner(abs(ast), rights):
                survivors.append(ast)
        else:  # moving right
            rights.append(ast)
​
    return survivors + rights

