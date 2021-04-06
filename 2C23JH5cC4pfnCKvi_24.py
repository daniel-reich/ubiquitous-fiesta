
def check_flush(table, hand):
    new_list = []
    second_list = []
    pattern_dictionary = {'S':0, 'H':0, 'D':0, 'C':0}
    for i in table:
        new_list.append(i.split("_"))
    print(new_list)
    for item in new_list:
        pattern_dictionary[item[1]] += 1
    for a in hand:
        second_list.append(a.split("_"))
    print(second_list)
    for b in second_list:
        pattern_dictionary[b[1]] += 1
    print(pattern_dictionary)
    for value in pattern_dictionary.values():
        print(value)
        if value >= 5:
            return True
        else:
            continue
    else:
        return False

