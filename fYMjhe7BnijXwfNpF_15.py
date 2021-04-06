
def stmid(string):
    lst = string.split(" ")
    result = ""
    for i in lst:
        if(len(i) % 2 == 0):
            result = result + i[0]
        else:
            result = result + i[int(len(i)/2)]
    return(result)

