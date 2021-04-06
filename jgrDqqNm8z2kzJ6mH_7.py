
tax = .06
​
​
def checkout(cart):
    res = sum([cart[x]['prc'] * cart[x]['qty'] if cart[x]['taxable'] is False
               else (cart[x]['prc'] * cart[x]['qty']) + (cart[x]['prc'] * cart[x]['qty']) * tax
               for x in range(len(cart))])
    return res

