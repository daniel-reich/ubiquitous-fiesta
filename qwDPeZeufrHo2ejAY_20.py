
def eval_algebra(x):
    izraz = x.split(' ')
    print(izraz)
    prvi = izraz[0]
    znak = izraz[1]
    drugi = izraz[2]
    rezultat = izraz[4]
    nepoznato = 0
    if prvi == "x":
        nepoznato = prvi
    elif drugi == "x":
        nepoznato = drugi
    else:
        nepoznato = rezultat
    resenje = 0
    if nepoznato == prvi:
        if znak == "+":
            resenje = int(rezultat) - int(drugi)
        elif znak == "-":
            resenje = int(rezultat) + int(drugi)
    if nepoznato == drugi:
        if znak == "+":
            resenje = int(rezultat) - int(prvi)
        elif znak == "-":
            resenje = int(prvi) - int(rezultat)
    if nepoznato == rezultat:
        if znak == "+":
            resenje = int(prvi) + int(drugi)
        elif znak == "-":
            resenje = int(prvi) - int(drugi)
​
    return resenje

