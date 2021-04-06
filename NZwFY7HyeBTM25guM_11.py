
def convert_to_decimal(perc):
    lst = []
    for itm in perc:
        itm = itm.strip("%")
        itm = float(itm) / 100
        lst.append(itm)
    return lst

