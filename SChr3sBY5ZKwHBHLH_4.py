
def sort_it(lst):
    ans = []
    while lst:
        m = lst[0]
        for i in lst:
            var_type = type(i).__name__
            min_type = type(m).__name__
            case1 = var_type == 'list' and min_type == 'list' and i[0] < m[0]
            case2 = var_type == 'list' and min_type == 'int' and i[0] < m
            case3 = var_type == 'int' and min_type == 'list' and i < m[0]
            case4 = var_type == 'int' and min_type == 'int' and i < m
            if (case1) or (case2) or (case3) or (case4):
              m = i
        ans.append(m)
        lst.remove(m)
    return ans

