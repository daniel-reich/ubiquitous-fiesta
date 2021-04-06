
def variable_valid(var):
    myans = var[0].isalpha()
    if myans:
        myans = var.count(' ') == 0
​
    return myans

