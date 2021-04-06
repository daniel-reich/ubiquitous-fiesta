
def overlap(s1, s2):
​
    second_word_index = 0
    second_word_array = [char for char in s2]
​
    for index in range(len(s1)):
​
        if s1[index] == s2[second_word_index]:
​
            del second_word_array[0]
​
            if second_word_index == len(s2) - 1 and index != len(s1) - 1:
                second_word_array = [char for char in s2]
                second_word_index = 0
​
            second_word_index += 1
​
        else:
​
            second_word_array = [char for char in s2]
            second_word_index = 0
​
    return s1 + "".join(second_word_array)

