
def remove_vowels(txt):
    table = str.maketrans(dict.fromkeys('aeiouAEIOU'))
    return txt.translate(table)

