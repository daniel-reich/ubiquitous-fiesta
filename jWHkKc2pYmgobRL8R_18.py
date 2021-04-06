
def distance_to_nearest_vowel(string):
    string = [0 if letter in ['a', 'e', 'i', 'o', 'u'] else 1 for letter in list(string) ]
    for index in range(len(string)):
        letter = string[index] 
        if letter == 1:
            current_min = len(string)
            for index2 in range(len(string)):
                if string[index2] == 0: 
                    if abs(index2 - index) < current_min:
                        current_min = abs(index2 - index)
            string[index] = current_min
    return string

