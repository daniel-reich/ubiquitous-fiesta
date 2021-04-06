
def look_and_say(start, n):
    j = 0
    last_array = []
    last_array.append(start)
    while j < n - 1:
        i = 0
        array = []
        while i < len(str(start)):
            array.append(str(start)[i])
            i += 1
        i = 0
        while True:
            try:
                if array[i][0] == array[i + 1]:
                    array[i] += str(array[i][0])
                    array.pop(i + 1)
                else:
                    i += 1
            except:
                break
        i = 0
        new_array = []
        while True:
            try:
                new_array.append(len(array[i]))
                new_array.append(array[i][0])
                i += 1
            except:
                break
        number = ''
        i = 0
        while True:
            try:
                number += str(new_array[i])
                i += 1
            except:
                break
        start = int(number)
        last_array.append(start)
        j += 1
    return last_array

