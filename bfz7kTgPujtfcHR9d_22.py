
def x_pronounce(sentence):
    result = ''
    index = 0
    for char in sentence:
        if char == 'x' and sentence[index - 1] == " " and sentence[index + 1] == " ":
            result += 'ecks'
            index += 1
        elif char == 'x' and sentence[index - 1] == " ":
            result += 'z'
            index += 1
        elif char == 'x':
            result += 'cks'
            index += 1
        else:
            result += char
            index += 1
    return result

