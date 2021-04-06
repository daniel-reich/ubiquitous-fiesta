
def XO(txt):
    x_count = 0
    o_count = 0
    answer = True
    for letter in txt:
        if letter == 'x' or letter == 'X':
            x_count += 1
        elif letter == 'o' or letter == 'O':
            o_count += 1
    if x_count == o_count:
        answer = True
    else:
        answer = False
    return answer

