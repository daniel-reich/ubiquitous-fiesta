
def split_into_buckets(string,size):
    words = string.split()
    array = []
    result_array = []
    counter = 0
    for word in words:
        length_of_array = 0
        for i in array:
            length_of_array += len(i)
        if len(word) > size:
            return []
        elif counter == 0:
            array.append(word)
        elif len(word) + length_of_array < size:
            array.append(" ")
            array.append(word)
        else:
            result_array.append("".join(array))
            array = []
            array.append(word)
        counter+=1
    list = []
    for i in result_array:
        x = i.split()
        for element in x:
            list.append(element)
    counter = len(list)
    remaining_items = []
    for i in range(0,len(words)-len(list),1):
        remaining_items.append(words[counter])
        counter+=1
    result_array.append(" ".join(remaining_items))
    return result_array

