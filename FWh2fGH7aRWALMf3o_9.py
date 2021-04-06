
def cleave(string, lst):
    if string in lst:
        return string
    words_starting_here = ((string[:end],string[end:]) for end in range(len(string)) if string[:end] in lst)
    for word, remaining_string in words_starting_here:
        cleave_sub = cleave(remaining_string, lst)
        if  cleave_sub.replace(" ", "") == remaining_string:
            return '{} {}'.format(word, cleave_sub)
    return 'Cleaving stalled: Word not found'

