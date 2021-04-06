
def two_digit_sum(n):
    n_string = str(n)
    new_list = []
    for i in n_string:
        new_list.append(i)
    return int(new_list[0]) + int(new_list[1])

