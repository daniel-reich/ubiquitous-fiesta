
def insert_whitespace(txt):
    answer = ''
    for letter in txt:
        if letter.isupper():
            answer += ' {}'.format(letter)
        else:
            answer += letter
    return answer[1:]

