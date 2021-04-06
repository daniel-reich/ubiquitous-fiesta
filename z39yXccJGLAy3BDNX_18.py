
def flipping_bits(n):
    k = '{0:032b}'.format(n); new_string = str()
    for i in k:
        if i == "1": new_string += str(0)
        if i == "0": new_string += str(1)
​
    return int(new_string, 2)

