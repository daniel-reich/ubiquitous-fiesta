
def hex_lattice(n):
    lattices = [0,1]
    index = 1
    while lattices[-1] < n:
        lattices.append(lattices[-1]+6*index)
        index+=1
    if n not in lattices: return "Invalid"
    returnLattice = ""
    minOs = lattices.index(n)
    maxOs = minOs*2-1
    rowLength = maxOs*2+1
    row = 1
    midRow = maxOs/2 + 0.5
    while row <= maxOs:
        if row < maxOs/2:
            numOs = minOs + row - 1 
        elif row > maxOs/2:
            numOs = maxOs - (row-midRow)
        else:
            numOs = maxOs
        
        
        Oindex = 0
        Ostring = " "
        while Oindex < numOs:
            Ostring += "o "
            Oindex  += 1
            
        
        if len(Ostring) < rowLength:
            spaces = ""
            spaceCount = int((rowLength - len(Ostring))/2)
            for each in range(0, spaceCount):
                spaces+=" "
            Ostring = spaces + Ostring + spaces
        
        if row != maxOs:
            Ostring += "\n"
        
        returnLattice += Ostring
            
        row+=1   
    
    return returnLattice

