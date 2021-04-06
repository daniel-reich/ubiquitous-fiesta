
def pricey_prod(d):
    wprice = sorted([[y, x] for x, y in d.items() if y >= 500], reverse=True)
    pricey = []
    for i in wprice:
        pricey.append(i[1])
    return pricey

