
def digits( numb ):
    strnumb = str( numb )
    place = len( strnumb ) 
​
    total = (numb - 10**(place-1))*place
    place -= 1
​
    while( place > 0 ):
        total += (9 * 10**(place-1))*(place)
        place -= 1
    
    return total

