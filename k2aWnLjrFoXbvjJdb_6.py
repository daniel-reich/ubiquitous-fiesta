
import re
from math import ceil
​
​
def letter_within_range(char_code):
    return chr(
        ((char_code - 65) % (91-65)) + 65)
​
​
def prepare_keyword(text, keyword):
    return (keyword*ceil(len(text)/len(keyword)))[0:len(text)].upper()
​
​
def vigenere(text, keyword):
    is_cipher_text = text.isupper()
    prepared_text = text if is_cipher_text else re.sub(
        '[^0-9a-zA-Z]+', '', text).upper()
    prepared_key = prepare_keyword(prepared_text, keyword)
​
    result = []
    for i in range(0, len(prepared_text)):
        starting_letter = ord(
            prepared_text[i] if is_cipher_text else prepared_key[i])
        distance_from_a = ord(
            prepared_key[i] if is_cipher_text else prepared_text[i]) - 65
​
        char_code = abs(
            starting_letter-distance_from_a) if is_cipher_text else starting_letter + distance_from_a
​
        result.append(letter_within_range(char_code))
    return ''.join(result)

