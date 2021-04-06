
def percent_filled(box):
    empty = sum(row.count(' ') for row in box)
    filled = sum(row.count('o') for row in box)
    return str(int(filled/(empty + filled)*100))+'%'

