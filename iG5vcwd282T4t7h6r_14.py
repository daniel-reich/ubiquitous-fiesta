
def str_to_dict(lst):
    my_dict={}
    for i in range(len(lst)):
        x = lst[i].split("=")
        my_dict[x[0]] = x[1]
    return my_dict

