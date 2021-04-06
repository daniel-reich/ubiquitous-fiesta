
def back_to_home(directions):
    n = directions.count('N')
    e = directions.count('E')
    s = directions.count('S')
    w = directions.count('W')
    
    if n == s and e == w:
        return True
    return False

