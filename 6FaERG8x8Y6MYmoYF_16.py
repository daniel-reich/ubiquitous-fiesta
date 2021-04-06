
def dice_score(lis):
    kecevi = lis.count(1)
    dvojke = lis.count(2)
    trojke = lis.count(3)
    cetvorke = lis.count(4)
    petice= lis.count(5)
    sestice = lis.count(6)
    suma = 0
    if kecevi > 2:
        suma += 1000
        kecevi -= 3
    if kecevi > 0:
        suma += kecevi*100
    if dvojke > 2:
        suma += 200
    if trojke > 2:
        suma += 300
    if cetvorke > 2:
        suma += 400
    if petice > 2:
        suma += 500
        petice -= 3
    if petice > 0:
        suma += petice*50
    if sestice > 3:
        suma += 600
    return suma

