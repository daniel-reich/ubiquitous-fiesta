
def binary_to_decimal(lst):
    nr = 0
    for i in range(len(lst)):
        nr += lst[i] * 2 ** (7-i)
    return nr

