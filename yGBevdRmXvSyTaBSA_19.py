
def sort_drinks_by_price(drinks):
    c= sorted([(drinks[i]["price"],drinks[i]) for i in range(len(drinks))])
    return [j for i,j in c]

