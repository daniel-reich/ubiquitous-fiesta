
def count_datatypes(*args):
    l = []
    int_count = 0
    str_count = 0
    bool_count = 0
    list_count = 0
    tuple_count = 0
    dictionary_count = 0
    for a in args:
        if type(a) is dict:
            dictionary_count += 1
        if type(a) is int:
            int_count += 1
        if type(a) is str:
            str_count += 1
        if type(a) is bool:
            bool_count += 1
        if type(a) is list:
            list_count += 1
        if type(a) is tuple:
            tuple_count += 1
    return [int_count, str_count, bool_count, list_count, tuple_count, dictionary_count]

