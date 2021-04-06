
def inator_inator(inv):
    for i in 'aeiouAEIOU':
        if inv.endswith(i):
            return inv + "-inator " + str(len(inv)) + '000'
    return inv + "inator " + str(len(inv)) + '000'

