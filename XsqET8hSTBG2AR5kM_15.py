
def letter_distance(txt1,txt2):
    final_array = []
    sum = 0
    list_1 = list(txt1)
    list_2 = list(txt2)
    if len(list_1) > len(list_2):
        for i in range(len(list_2)):
            a = ord(list_1[i])
            b = ord(list_2[i])
            c = a - b
            final_array.append(abs(c))
        d = len(list_1) - len(list_2)
        final_array.append(abs(d))
    elif len(list_1) == len(list_2):
        for i in range(len(list_2)):
            a = ord(list_1[i])
            b = ord(list_2[i])
            c = a - b
            final_array.append(abs(c))
    else:
        for i in range(len(list_1)):
            a = ord(list_1[i])
            b = ord(list_2[i])
            c = a - b
            final_array.append(abs(c))
        d = len(list_2) - len(list_1)
        final_array.append(abs(d))
    for i in range(len(final_array)):
        sum = sum + final_array[i]
    return sum

