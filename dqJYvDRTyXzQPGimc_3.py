
def is_unfair_hurdle(hurdles):
    if len(hurdles) >= 4:
        return True
    
    posts = [i for i in range(len(hurdles[0])) if hurdles[0][i] == '#']
    if posts[1]-posts[0] < 4:
        return True
    else:
        return False

