
def bracket_logic(xp):
    #brainstorm#
    expecting = [] #latest (-1) is the one that the parser is expecting to be correct
    pOpening = '(<[{'
    pClosing = ')>]}'
    pExchange = {'(':')', '<':'>','[':']','{':'}'}
    print(xp)
    for _ in xp:
        print(expecting)
        if _ in pOpening:
            expecting.append(_)
        if _ in pClosing:
            if len(expecting) > 0:
                if pExchange[expecting[-1]] == _:
                    expecting.pop()
                else:
                    return False
            else:
                return False
    if len(expecting) > 0:
        return False 
    return True

