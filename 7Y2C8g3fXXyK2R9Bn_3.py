
def keyword_cipher(key, message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    value_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                  'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                  'x': 24, 'y': 25, 'z': 26}
    removed_keys = []
    dupe_keys = []
    lower_key = key.lower()
    final_keys = []
    lower_message = message.lower()
    for letter in lower_key:
        if letter not in removed_keys:
            try:
                alphabet.remove(letter)
                removed_keys.append(letter)
            except KeyError:
                print("Key not in alphabet")
​
    for letter in lower_key:
        if letter not in dupe_keys:
            final_keys.append(letter)
            dupe_keys.append(letter)
    final_keys = final_keys[::-1]
​
    for letter in final_keys:
        alphabet.insert(0, letter)
​
​
    output_string = ""
    for letter in lower_message:
        if letter in alphabet:
            output_string = output_string + alphabet[value_dict[letter]-1]
        else:
            output_string = output_string + letter
​
    return output_string.lower()

