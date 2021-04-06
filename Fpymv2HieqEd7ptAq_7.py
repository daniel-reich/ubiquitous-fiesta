
def split(txt):
    count = 0
    new_element = ''
    new_list = []
    for elem in txt:
        new_element += elem
        if elem == '(':
            count += 1
        if elem == ')':
            count -= 1
        if count == 0:
            new_list.append(new_element)
            new_element = ''
    return new_list

