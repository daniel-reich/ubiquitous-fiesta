
def happy_birthday(age):
    div, mod = divmod(age, 2)
    if mod == 0:
        age = str(20) + ', '
    else:
        age = str(21) + ', '
    return 'Mubashir is just ' + age + 'in base ' + str(div) + '!'

