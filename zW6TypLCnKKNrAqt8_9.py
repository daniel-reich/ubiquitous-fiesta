
def left_side(lst):
    new_list = [0]
    position = 1
    for i in lst[1:]:
        count = 0
        index = 0
        while index < position:
            if i > lst[index]:
                count += 1
            index += 1
        new_list.append(count)
        position += 1
    return new_list
​
​
def right_side(lst):
    lst.reverse()
    new_list = left_side(lst)
    new_list.reverse()
    return new_list

