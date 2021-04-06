
def edabit_in_string(txt):
    counter = 0
    word = ''
    for i in txt:
        if i == 'edabit'[counter]:
            word += i
            counter += 1
        if word == 'edabit':
            break
    return 'YES' if word == 'edabit' else 'NO'

