
def change(el):
    if type(el) == bool:
        return not el
    if type(el) == int:
        return el + 1 if el % 2 == 0 else el
    return el[0].upper() + el[1:] + '!'
​
def change_types(lst):
    return [change(el) for el in lst]

