
def happy_birthday(age):
    if age % 2 == 0:
        base = age // 2
        return "Mubashir is just 20, in base " + str(base) + "!"
    else:
        base = (age - 1) // 2
        return "Mubashir is just 21, in base " + str(base) + "!"

