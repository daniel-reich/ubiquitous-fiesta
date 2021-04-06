
def mathematical(exp, numbers):
    final_array = []
    array = []
    array.append(exp[5:6])
    array.append(exp[6:7])
    array.append(exp[7:])
    for number in numbers:
        result = 0
        if array[1] == '+':
            result += number + int(array[2])
        elif array[1] == '-':
            result += number - int(array[2])
        elif array[1] == '^':
            result += number**int(array[2])
        elif array[1] == 'x':
            result += number*int(array[2])
        elif array[1] == '/':
            result += int(number/int(array[2]))
        final_array.append("f({})={}".format(number, result))
    return final_array

