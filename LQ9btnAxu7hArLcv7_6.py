
def diagonalize(n, d):
    final_list = []
    for x in range(n):
        temp_list = [y for y in range(x, n + x)]
        if d[1] == 'r':
            temp_list.reverse()
        if d[0] == 'u':
            final_list.append(temp_list)
        else:
            final_list.insert(0, temp_list)
    return final_list

