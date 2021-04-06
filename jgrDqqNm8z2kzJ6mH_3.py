
def checkout(cart):
    nontaxable = sum(p["prc"]*p["qty"] for p in cart if not p["taxable"])
    taxable = sum(p["prc"]*p["qty"] for p in cart if p["taxable"])
    return taxable*1.06 + nontaxable

