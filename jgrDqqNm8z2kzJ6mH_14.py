
tax = {True: 0.06, False: 0.0}
​
def checkout(cart):
    ans = 0
    for item in cart:
        ans += item["prc"] * item["qty"] * (1 + tax[item["taxable"]])
    return ans

