
def split_code(item):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
​
    arr_alpha = []
    arr_number = []
​
    for i in item:
        if i in alpha:
            arr_alpha.append(i)
        else:
            arr_number.append(i)
​
    return ["".join(arr_alpha), int("".join(arr_number))]

