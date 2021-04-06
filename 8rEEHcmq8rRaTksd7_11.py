
def lines_are_parallel(l1, l2):
    if int(l1[0])==int(l2[0])==0:
        return True
    elif (int(l1[1])/int(l1[0]))==(int(l2[1])/int(l2[0])):
        return True
    else:
        return False

