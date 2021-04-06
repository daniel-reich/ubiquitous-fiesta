
def unique_lst(lst):
    output = []
    for i in lst:
        if i not in output and i > 0:
            output.append(i)
    return output

