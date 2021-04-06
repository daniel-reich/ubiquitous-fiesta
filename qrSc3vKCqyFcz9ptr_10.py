
def sum_round(num):
    str_number = str(num)
    newlist = []
    for i in range(len(str_number)):
        if str_number[i] == '0':
            continue
        else:
            newlist.append(str_number[i] + ('0' * len(str_number[i+1:])))
    return ' '.join(newlist[::-1])

