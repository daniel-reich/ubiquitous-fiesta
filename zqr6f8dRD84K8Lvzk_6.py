
import math
​
def hex_lattice(n):
    for num in range(n + 1):
        hexagonalVal = 1 + 6*((num*(num-1))/2)
        if hexagonalVal == n:
            break
        elif hexagonalVal > n:
            return "Invalid"
​
    hexagonalRoot = int((3 + math.sqrt(12*n - 3))/6)
    
    height = 2*hexagonalRoot - 1
    rowLen = 4*hexagonalRoot-1
    
    dots = hexagonalRoot
    spaceAmt = hexagonalRoot
    spaceAccom = 0
​
    idx1 = -1
    idx2 = 1
​
    string = ''
​
    i = 0
    while i < height:
        j = 0
        while j < rowLen:
            if j != spaceAmt:
                string += ' '
            else:
                k = 0
                while k < dots:
                    if k != dots - 1:
                        string += 'o '
                    else:
                        string += 'o'
                    k += 1
                j = 3*hexagonalRoot-2 + spaceAccom
                
            j += 1
        
        if i != height - 1:
            string += '\n'
​
        dots += idx2
        spaceAccom += idx2
        spaceAmt += idx1
        if spaceAmt == 1:
            idx1 = 1
            idx2 =- 1
​
        i += 1
​
    return string

