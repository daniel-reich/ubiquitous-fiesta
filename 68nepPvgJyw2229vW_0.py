
def get_ASCII(ele_list):
    dictionary = {}
    for i in range(0, len(ele_list)):
        result = 0
        for j in str(ele_list[i]):
            result += ord(str(j))
        dictionary[i] = result
​
    lst = sorted(dictionary.items(), key=lambda x: (x[1], -x[0]))
    return lst[-1][0]
​
​
def pairwise_swap(list_of_elements):
    if len(list_of_elements) % 2 == 0:
        for i in range(0, len(list_of_elements), 2):
            list_of_elements[i], list_of_elements[i + 1] = list_of_elements[i + 1], list_of_elements[i]
​
    else:
        for i in range(0, len(list_of_elements) - 1, 2):
            list_of_elements[i], list_of_elements[i + 1] = list_of_elements[i + 1], list_of_elements[i]
        index = get_ASCII(list_of_elements)
        list_of_elements[-1], list_of_elements[index] = list_of_elements[index], list_of_elements[-1]
    return list_of_elements

