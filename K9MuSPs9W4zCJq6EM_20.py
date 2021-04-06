
def simplify_problem(lst, n):
    s_list = [lst.index(i) for i in sorted(lst)]
    s_n = s_list[lst.index(n)]
    return s_list, s_n
​
​
def swap(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst
​
​
def find_and_swap(lst, n, count=1):
    # lst = [0, 2, 3, 1, 4]
    # n = 2
    print('Problem: {}'.format((lst, n)))
    origin_index = lst.index(n)
    target_index = n
    print('Origin: {}  ' 'Target: {}'.format(origin_index, target_index))
​
    if origin_index == target_index:
        print('Origin == Target --> break')
        count = 0
​
    lst = swap(lst, origin_index, target_index)
    # lst.insert(target_index, lst.pop(origin_index))
    print('Swapped: {}'.format((lst, lst[origin_index])))
    return lst, lst[origin_index], count
​
​
def cycle_length(lst, n):
    simple_list, simple_n = simplify_problem(lst, n)
    counter = 0
    while True:
        simple_list, simple_n, count = find_and_swap(simple_list.copy(), simple_n)
        if count:
            counter += 1
        else:
            break
    return counter

