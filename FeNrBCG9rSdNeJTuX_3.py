
def max_possible(n1, n2):
    n1_str_list = list(str(n1))
    n2_str = str(n2)
​
    n2_str_sorted = sorted(n2_str, reverse=True)
​
    i = 0
    j = 0
    while i < len(n1_str_list) and j < len(n2_str_sorted):
        if int(n1_str_list[i]) < int(n2_str_sorted[j]):
            n1_str_list[i] = n2_str_sorted[j]
            j = j + 1
        i = i + 1
​
    return int(''.join(n1_str_list))

