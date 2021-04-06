
def unique_styles(my_list):
    tmp_list = []
    for i in my_list:
        tmp = i.split(",")
        for j in tmp:
            tmp_list.append(j)
    return len(set(tmp_list))

