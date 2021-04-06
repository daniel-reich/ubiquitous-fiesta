
def vowels(string):
    if not string:
        return 0
    return (1 if string[0] in 'aeiouAEIOU' else 0) + vowels(string[1:])

