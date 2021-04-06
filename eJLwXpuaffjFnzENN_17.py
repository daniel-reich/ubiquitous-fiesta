
def find_even_nums(num):
    num_list = []
    for i in range(num):
        i += 1
        even_test = i % 2
        if even_test == 0:
            num_list.append(i)
    return num_list

