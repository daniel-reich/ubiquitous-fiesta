
def get_discounts(nums, d):
    x = "0."+ d.replace("%", "")
    discount = float(x)
    lista = []
    for n in nums:
        lista.append(n * discount)
    return lista

