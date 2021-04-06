
def percentage_changed(old, new):
    old_price = int(old[1:])
    new_price = int(new[1:])
    if old_price > new_price:
        perc_change = round((old_price - new_price)/old_price *100)
        return str(perc_change) + "% "+"decrease"
    else:
        perc_change = round((new_price - old_price)/old_price * 100)
        return str(perc_change) + "%" + " increase"

