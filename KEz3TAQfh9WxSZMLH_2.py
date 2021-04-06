
def count_all(txt):
    dict = {'LETTERS': 0, 'DIGITS': 0}
    for char in txt:
        if char.isalpha():
            dict['LETTERS'] += 1
        if char.isdigit():
            dict['DIGITS'] += 1
    return dict

