
def flick_switch(lst):
    state = True
    newLst = []
    for item in lst:
        if item == "flick":
            if state == True:
                state = False
            else:
                state = True
        newLst.append(state)
    return newLst

