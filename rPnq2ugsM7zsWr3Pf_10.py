
def find_all_digits(lst):
    dig = ''.join([str(j) for j in lst])
    i = max([dig.find(str(j)) for j in range(10)])
    return lst[(i//4)] if len(set(dig)) == 10 else "Missing digits!"

