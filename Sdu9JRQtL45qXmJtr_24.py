
def happy_birthday(age):
    for bas in range(10,age):
        if 2*bas==age: return'Mubashir is just 20, in base {}!'.format(bas)
        if 2*bas+1==age: return'Mubashir is just 21, in base {}!'.format(bas)

