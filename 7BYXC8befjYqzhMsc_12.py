
def classify_rug(pattern):
    h = horizontal_check(pattern)
    v = vertical_check(pattern)
    if h and v:
        return 'perfect'
    elif h:
        return 'horizontally symmetric'
    elif v:
        return 'vertically symmetric'
    else:
        return 'imperfect'
​
​
​
def horizontal_check(pattern):
    if len(pattern) % 2 == 0:
        #dont do any operations on the division by 2
        if sorted([x for x in pattern[0:len(pattern)//2]]) == sorted([x for x in pattern[len(pattern)//2:]]):
            return True
        else:
            return False
​
    elif len(pattern) % 2 != 0:
        pattern.pop((len(pattern)-1)//2)
        return horizontal_check(pattern)
​
​
def vertical_check(pattern):
    
    try:
        len(pattern[0])
    except:
        return True
        
    if len(pattern[0]) % 2 == 0:
        if sorted([ row[0:len(row)//2] for row in pattern  ]) == sorted([ row[len(row)//2:] for row in pattern]):
            return True
        else:
            return False
​
    elif len(pattern[0]) % 2 != 0:
        popping = (len(pattern[0]) - 1) //2
        for x in range(len(pattern)):
            pattern[x].pop(popping)
        return vertical_check(pattern)

