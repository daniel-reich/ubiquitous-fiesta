
def quad_sequence(lst):
    diff_1 = lst[1] - lst[0]
    diff_2 = lst[2] - lst[1]
    quad_diff = (diff_2 - diff_1)
    last_diff = lst[-1] - lst[-2]
​
    copy = list(lst)
    i = 0
    while i < len(lst):
        copy.append(copy[-1]+last_diff+(i+1)*quad_diff)
        i += 1
    return copy[len(lst):len(copy)]

