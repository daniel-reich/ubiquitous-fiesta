
def freq_count(lst, el):
    lst = str(lst)[1:-1].replace(' ', '').replace(',', ' ').replace('[', ' [ ').replace(']', ' ] ').replace('  ', ' ').split()
    print(lst)
    result = [[0, 0]]
    count = 0
    for i in lst:
        if i == '[':
            count += 1
            if len(result) - 1 < count:
                result.append([count, 0])
        elif i == str(el):
            result[count][1] += 1
        elif i == ']':
            count -= 1
    return result

