
def longest_substring(digits):
    lst = []
    ind = []
    count = 0
    binary = [1 if i else 0 for i in [int(i) % 2 == 0 for i in digits]]
    for i in range(len(binary) - 1):
        if binary[i + 1] - binary[i] != 0:
            count += 1
            if i == 28:
                ind.append(i)
                lst.append(count)
        else:
            ind.append(i)
            lst.append(count)
            count = 0
    lst = [i + 1 for i in lst]
    ind = [i + 1 for i in ind]
​
    length_index = lst.index(max(lst))
​
    if length_index == 0:
        starting_index = 0
    else:
        starting_index = ind[length_index - 1]
​
    return digits[starting_index : max(lst) + starting_index]

