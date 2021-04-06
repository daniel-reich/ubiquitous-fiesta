
def list_operation(x, y, n):
    range_list = range(x, y + 1)
    main_list = []
    for i in range_list:
        if i % n == 0:
            main_list.append(i)
    return main_list

