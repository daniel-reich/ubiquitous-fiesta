
def double_swap(string, c1, c2):
    string, counter = list(string), 0
    for i in string:
        if i == c1:
            string[counter] = c2
        if i == c2:
            string[counter] = c1
        counter += 1
    return "".join(string)

