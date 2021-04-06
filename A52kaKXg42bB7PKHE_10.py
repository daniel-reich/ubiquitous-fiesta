
def num_then_char(lst):
    num_list, str_list, len_list = [], [], []
    for slist in lst:
        len_list.append(len(slist))
        for item in slist:
            if type(item) is int or type(item) is float:
                num_list.append(item)
            else:
                str_list.append(item)
    num_list.sort()
    str_list.sort()
    num_list.extend(str_list)
    return_list = []
    for i in range(len(len_list)):
        temp_list = [item for n, item in enumerate(num_list) if n < len_list[i]]
        return_list.append(temp_list)
        del num_list[0:len_list[i]]
    return return_list

