
def get_prices(lst):
    return [float(l.split( "(")[1].split(")")[0].replace("$", "")) for l in lst]

