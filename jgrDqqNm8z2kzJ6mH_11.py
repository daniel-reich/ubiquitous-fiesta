
tax = .06
​
​
def checkout(cart):
    t = 0
    for d in cart:
        calc = d['prc'] * d['qty']
        t += (calc * tax) + calc if d['taxable'] else calc
    return t

