
def skip_the_sugar(drinks):
    lst = []
    for i in drinks:
        if i not in ["cola", "fanta"]:
            lst.append(i)
    return lst

