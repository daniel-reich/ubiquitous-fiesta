
def vigenere(string1, key1):
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    alpha_dict = {'A' : 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                   'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
​
    answer = ''
    stripped = ''.join([x for x in string1.lower() if x in letter_list]).upper()
    key2 = ''
    i = 0
    for x in range(0, len(stripped)):
        key2 = key2 + key1[i].upper()
        i += 1
        if i > len(key1) - 1:
            i = 0
​
    if string1[-1] not in alpha_dict.keys():
        print(stripped)
        print(key2)
        for letter1 in enumerate(stripped):
            total = alpha_dict[letter1[1]] + alpha_dict[key2[letter1[0]]] - 1
            total = total - 26 if total > 26 else total
            answer = answer + letter_list[total - 1]
        return answer.upper()
​
    else:
        print(stripped)
        print(key2)
        for letter2 in enumerate(string1):
            answer = answer + letter_list[alpha_dict[letter2[1]] - alpha_dict[key2[letter2[0]]]]
        return answer.upper()

