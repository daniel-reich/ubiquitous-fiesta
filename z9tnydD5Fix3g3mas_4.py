
def check_pattern(arrays,string):
    x = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_array = list(x)
    if len(arrays) != len(string):
        return False
    word = []
    for i in range(0,len(arrays),1):
        word.append(alphabet_array[i])
    index_position0 = 0
    for array0 in arrays:
        index_position1 = 0
        for array1 in arrays:
            if array0 == array1:
                word[index_position1] = word[index_position0]
            index_position1 += 1
        index_position0 += 1
    letter_index = 0
    index_position = 0
    for letter in word:
        if letter == alphabet_array[letter_index]:
            letter_index += 1
        elif word[index_position] == word[index_position-1]:
            pass
        else:
            word[index_position] = alphabet_array[letter_index]
        index_position+=1
    index_position0 = 0
    for array0 in arrays:
        index_position1 = 0
        for array1 in arrays:
            if array0 == array1:
                word[index_position1] = word[index_position0]
            index_position1 += 1
        index_position0 += 1
​
    if "".join(sorted(word)).lower() == "".join(sorted(string)).lower() :
        return True
    return False

