
def completely_filled(lst):
    for i in lst:
        for j in i:
            if j == " ":
                return(False)
    return(True)

