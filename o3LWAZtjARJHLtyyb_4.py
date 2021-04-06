
import string
​
def reverse_case(txt):
​
    upper_letters = string.ascii_uppercase
​
    transformed_letters = [char.lower() if char in upper_letters
                           else char.upper()
                           for char in txt]
​
    return ''.join(transformed_letters)

