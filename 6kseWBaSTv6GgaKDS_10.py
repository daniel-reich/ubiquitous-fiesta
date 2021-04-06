
def next_letters(s):
    lst = list(s)[::-1] + ['']
    for idx, v in enumerate(lst):
        if v == '':
            lst[idx] = 'A'
            return ''.join(lst[::-1])
        if v != 'Z':
            lst[idx] = chr(ord(v) + 1)
            return ''.join(lst[::-1])
        else:
            lst[idx] = 'A'

