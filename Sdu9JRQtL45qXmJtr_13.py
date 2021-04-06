
def happy_birthday(age):
    rem, base = (1, (age - 1) // 2) if age % 2 else (0, age // 2)
    return "Mubashir is just 2{}, in base {}!".format(rem, base)

