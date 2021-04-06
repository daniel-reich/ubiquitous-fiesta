
def checkout(cart):
    [total,itotal] = [0,0]
    for item in cart:
        if item["taxable"]:
            itotal = item['prc']*item["qty"]
            itotal+=itotal*0.06
        else:itotal+=item['prc']*item["qty"]
        total +=itotal
        itotal=0
    return total

