
def separate_numbers(s):
    str_number = str(s)
    temp_str_number = str_number
    newlist = []
    future_number = 0
    for i in range(len(str_number)):
        for j in range(len(str_number)):
            try:
                number = str_number[i:j]
                newlist.append(number)
                future_number = int(number)+1
                if str(future_number) in temp_str_number:
                    temp_str_number = temp_str_number[j:]
                    while str(future_number) in str_number:
                        newlist.append(str(future_number))
                        future_number += 1
                    if len(''.join([x for x in newlist])) == len(s):
                        return 'YES {}'.format(number)
                    else:
                        newlist = []
            except ValueError as err:
                pass
    return 'NO'

