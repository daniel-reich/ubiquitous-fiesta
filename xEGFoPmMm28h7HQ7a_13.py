
def letter_combinations(digits): 
    letters_numbers_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                            '8': ['t', 'v', 'u'], '9': ['w', 'x', 'y', 'z'], }
​
    letters_list = []
    letters_combinations_list = []
​
    for i in range(len(digits)):
        if digits[i] in letters_numbers_dict.keys():
            letters_list.append(letters_numbers_dict[digits[i]])
​
    if len(digits) == 2:
        for i in range(len(letters_list[0])):
            for j in range(len(letters_list[1])):
                letters_combinations_list.append(letters_list[0][i]+letters_list[1][j])
​
    elif len(digits) == 3:
        for i in range(len(letters_list[0])):
            for j in range(len(letters_list[1])):
                for l in range(len(letters_list[2])):
                    letters_combinations_list.append(letters_list[0][i]+letters_list[1][j]+letters_list[2][l])
​
    return letters_combinations_list

