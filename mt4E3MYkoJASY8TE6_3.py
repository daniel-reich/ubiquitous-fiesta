
def combo_list_of_string(lst_of_strs):
    if len(lst_of_strs) == 0:
        return ['']
    result = []
    for i in range(0, len(lst_of_strs)):
        for j in range(len(lst_of_strs[i])):
            to_add_letter = lst_of_strs[i][j]
            remain_lst_of_strs = lst_of_strs[i + 1:]
            for string in combo_list_of_string(remain_lst_of_strs):
                if len(string) == len(lst_of_strs) - 1:
                    result.append(to_add_letter + string)
    return result
​
def crack_pincode(pincode):
    adj_dct = {"1": "124", "2": "1235", "3": "236", "4": "1475",
               "5": "24568", "6": "3569", "7": "478", "8": "57890",
               "9": "689", "0": "80"}
    if len(pincode) == 0:
        return []
    lst_of_strs = []
    for i in range(len(pincode)):
        lst_of_strs.append(list(adj_dct[pincode[i]]))
    print(lst_of_strs)
    return sorted(combo_list_of_string(lst_of_strs))

