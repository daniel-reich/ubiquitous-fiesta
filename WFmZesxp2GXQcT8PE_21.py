
from itertools import cycle
​
​
def digital_cipher(message, key):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
     'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
     'z': 26}
    char_map = [d[char] for char in message]
​
    key_list = [int(x) for x in str(key)]
    zip_list = list(zip(char_map, cycle(key_list)))
​
    return [i + j for i, j in zip_list]
​
print(digital_cipher("scout", 1939))

