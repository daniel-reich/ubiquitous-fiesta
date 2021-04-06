
def will_hit(equation, position):
    kvalue = equation.split()[2][0:-1]
    mvalue = equation.split()[3]+equation.split()[4]
    if (int(kvalue)*position[0]+int(mvalue)) == position[1]:
        return True
    else:
        return False

