
def checkout(cart, tax=0.06):
    return round(sum(item["prc"] * item["qty"] * (1 + (tax if item["taxable"]
                                                       else 0))
                     for item in cart), 2)

