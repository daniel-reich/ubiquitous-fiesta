
def num_in_str(lst):
    return [i for i in lst if any(map(str.isdigit, i))]

