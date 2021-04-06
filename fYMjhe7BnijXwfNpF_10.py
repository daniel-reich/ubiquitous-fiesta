
def stmid(string):
    lista = string.split(" ")
    strf = ''
    for item in lista:
        if len(item)%2 ==0:
            strf += item[0]
        else:
            strf += item[len(item)//2]
    return strf

