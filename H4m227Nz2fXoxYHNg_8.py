
def list_values_types(lst):
    t_list = []
    o_t = ""
    for i in lst:
        o_t = str(type(i))
        o_t = o_t.strip("<class ").strip(">").strip("''")
        t_list.append(o_t)
    return t_list

