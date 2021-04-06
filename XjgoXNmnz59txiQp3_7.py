
def split(number):
    list = []
    result = 1
    while 1:
        if number-3>1:
            number -=3
            list.append(3)
        else:
            list.append(number)
            break
    for i in list:
        result = result * i
    return result

