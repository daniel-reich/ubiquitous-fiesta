
def vowels(string):
    if len(string) == 0:
        return 0
    if string[0] in 'aeiou':
        return 1 + vowels(string[1:])
    else:
        return vowels(string[1:])

