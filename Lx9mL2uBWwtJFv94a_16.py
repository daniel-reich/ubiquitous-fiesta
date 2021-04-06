
def checker_board(size:int, El1, El2) -> list:
    
    if El1 == El2: return "invalid"
    
    EV = []
    for x in range(size):
        if x % 2 == 0:
            R1 = list("{0}{1}".format(El1, El2)*(size+1))[0:size]
            if type(El1) == int and type(El2) == int:
                R1 = [int(i) for i in R1]
            EV.append(R1)
        else:
            R1 = list("{1}{0}".format(El1, El2)*(size+1))[0:size]
            if type(El1) == int and type(El2) == int:
                R1 = [int(i) for i in R1]
            EV.append(R1)
        x += 1
    return EV

