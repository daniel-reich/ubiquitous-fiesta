
def tidy_books(lst: list) -> list:
    temp = [ j.strip().split(' - ') for i in lst for j in i]
    return temp

