
def two_product(lst, n):
    mods = [i for i in sorted(lst) if i!=0 and not (n%i)]
    products = [i for i in mods if (n / i) in lst]
    return products if products else None

