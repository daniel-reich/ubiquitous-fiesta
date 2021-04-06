
def pyramid_lists(n):
    n_range = list(range(1, n + 1))
    output = []
    for list_values in n_range:
        list_length = []
        for thing in range(list_values):
            list_length.append(list_values)
        output.append(list_length)
    return output

