
def three_letter_collection(word):
    result = []
    max_index = 2
    if len(word) >= 3:
        while max_index < len(word):
            new_string = ''
            new_string += word[max_index - 2] + word[max_index - 1] + word[max_index]
            result.append(new_string)
            max_index += 1
    result.sort()
    return result

