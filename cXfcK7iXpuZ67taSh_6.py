
def mystery_func(txt):
    letters = txt[::2]
    nums = txt[1::2]
    final = []
    for i in zip(letters, nums):
        final.append(i[0]*int(i[1]))
    return ''.join(final)

