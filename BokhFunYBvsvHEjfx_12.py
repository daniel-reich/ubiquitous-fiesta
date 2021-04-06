
def seven_boom(lst):
    for i in lst:
        for j in str(i):
            if int(j)==7:
               return("Boom!")
    return("there is no 7 in the list")

