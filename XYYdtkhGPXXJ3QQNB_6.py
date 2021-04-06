
def num_in_str(lst):
    return [i for i in lst if any(n in i for n in list('1234567890'))]

