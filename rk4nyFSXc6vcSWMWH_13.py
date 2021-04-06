
def shared_digits(array):
    for i in range(len(array)-1):
        flag, temp0, temp1 = False, list(str(array[i])), list(str(array[i+1]))
        if True not in [True for e in temp0 if e in temp1]:
            return False
    return True

