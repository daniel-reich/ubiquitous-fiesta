
def count_datatypes(*args):
    final_list = []
    final = []
    my_list = [int, str, bool, list, tuple, dict]
    for i in range (0,len(args)):
        final_list.append(type(args[i]))
    #print(final_list)
    int_count = final_list.count(int)
    final.append(int_count)
    str_count = final_list.count(str)
    final.append(str_count)
    bool_count = final_list.count(bool)
    final.append(bool_count)
    list_count = final_list.count(list)
    final.append(list_count)
    tuple_count = final_list.count(tuple)
    final.append(tuple_count)
    dict_count = final_list.count(dict)
    final.append(dict_count)
    
    return final
    
    
​
print(count_datatypes(1, 45, "Hi", False))

