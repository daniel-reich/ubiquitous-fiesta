
def cap_space(string):
    new_string = str()
    for letter in string:
        if letter.isupper():
            new_string += ' ' + str(letter.lower())
        else:
            new_string += letter
​
    return new_string

