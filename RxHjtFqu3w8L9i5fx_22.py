
def bell(num):
    array = [[1],
             [1, 2]]
    number = 3
    while number <= num:
        array.append([])
        array[number -1].append(array[number - 2][number -2])
        for i in range(1, number):
            array[number -1].append(array[number -1][i -1] + array[number -2][i -1])
        number += 1
    return array[num -1][num -1]

