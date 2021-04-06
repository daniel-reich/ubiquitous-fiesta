
def longest_nonrepeating_substring(txt):
    lst_sub = []
    for i in range(len(txt)):
        cache_list = []
        j = i + 1
        cache_list.append(txt[i])
        while j < len(txt) and txt[j] not in cache_list:
            cache_list.append(txt[j])
            j += 1
        lst_sub.append(cache_list)
    cl = [len(i) for i in lst_sub]
    op_lst = lst_sub[cl.index(max(cl))]
    op_str = ""
    for c in op_lst:
        op_str += c
    return op_str

