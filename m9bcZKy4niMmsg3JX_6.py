
def society_name(friends):
    vege =""
    vege2 =""
    for i in friends :
        vege += i[0].upper()
    vege = sorted(vege)
    for i in vege:
        vege2 +=i
    return vege2

