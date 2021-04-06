
def jumping_frog(n, stones):
    count = 1
    frog = 0
    while frog < n:
        if not stones[frog]:
            return 'no chance :-('
        
        count += 1
        if stones[frog - stones[frog]] > stones[frog] and stones[frog+1] == 1:
            frog -= stones[frog]
        else:
            frog += stones[frog]
    
    return count

