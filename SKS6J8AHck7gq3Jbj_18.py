
def tidy_books(lst):
    new_list = []
    for i in lst:
        for y in i:
            x, y, z = (str(y).partition('-'))
            x, z = (x.strip(), z.strip())
            xz = [x, z]
            new_list.append(xz)
    return new_list

